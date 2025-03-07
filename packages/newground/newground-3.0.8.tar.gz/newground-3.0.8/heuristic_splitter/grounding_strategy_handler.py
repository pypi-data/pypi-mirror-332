
import io
import time
import sys
import os
import subprocess
import gc

#from memory_profiler import profile

import tempfile

from clingo.ast import ProgramBuilder, parse_string

from heuristic_splitter.graph_data_structure import GraphDataStructure

from heuristic_splitter.grounding_strategy_generator import GroundingStrategyGenerator
from heuristic_splitter.domain_transformer import DomainTransformer

from heuristic_splitter.graph_creator_transformer import GraphCreatorTransformer

from heuristic_splitter.grounding_approximation.approximate_generated_sota_rules import ApproximateGeneratedSotaRules
from heuristic_splitter.grounding_approximation.approximate_generated_bdg_rules import ApproximateGeneratedBDGRules

#from heuristic_splitter.grounding_approximation.approximate_generated_sota_rules_transformer import ApproximateGeneratedSotaRulesTransformer
from heuristic_splitter.grounding_approximation.approximate_generated_bdg_rules_transformer import ApproximateGeneratedBDGRulesTransformer
from heuristic_splitter.grounding_approximation.variable_domain_inference_transformer import VariableDomainInferenceTransformer

from heuristic_splitter.nagg_domain_connector_transformer import NaGGDomainConnectorTransformer
from heuristic_splitter.nagg_domain_connector import NaGGDomainConnector

from heuristic_splitter.program.preprocess_smodels_program import preprocess_smodels_program

from nagg.default_output_printer import DefaultOutputPrinter

from nagg.nagg import NaGG
from nagg.aggregate_strategies.aggregate_mode import AggregateMode
from nagg.cyclic_strategy import CyclicStrategy
from nagg.grounding_modes import GroundingModes
from nagg.foundedness_strategy import FoundednessStrategy
from heuristic_splitter.domain_inferer import DomainInferer

from heuristic_splitter.enums.grounding_strategy import GroundingStrategy
from heuristic_splitter.enums.sota_grounder import SotaGrounder
from heuristic_splitter.enums.output import Output
from heuristic_splitter.enums.cyclic_strategy import CyclicStrategy
from heuristic_splitter.enums.foundedness_strategy import FoundednessStrategy

from heuristic_splitter.program.string_asp_program import StringASPProgram
from heuristic_splitter.program.smodels_asp_program import SmodelsASPProgram

from cython_nagg.cython_nagg import CythonNagg
from cython_nagg.generate_head_guesses import GenerateHeadGuesses
from cython_nagg.justifiability_type import JustifiabilityType

from heuristic_splitter.logging_class import LoggingClass
from heuristic_splitter.cdnl.cdnl_data_structure import CDNLDataStructure

from ctypes import *
so_filename = "c_output_redirector.so"

# C-Struct (return value)
class PipeFds(Structure):
    _fields_ = [("read_end", c_int), ("write_end", c_int)]


class CustomOutputPrinter(DefaultOutputPrinter):

    def __init__(self):
        self.strings = []

    def custom_print(self, string):
        #print(string)
        self.strings.append(string)

    def get_string(self):
        return "\n".join(self.strings)

class GroundingStrategyHandler:

    def __init__(self, grounding_strategy: GroundingStrategyGenerator, rule_dictionary, graph_ds: GraphDataStructure, facts, query,
        debug_mode, enable_lpopt, sota_grounder = SotaGrounder.GRINGO,
        output_printer = None, enable_logging = False, logging_class: LoggingClass = None,
        output_type: Output = None, cdnl_data_structure: CDNLDataStructure = None, ground_and_solve=False,
        cyclic_strategy_used=CyclicStrategy.USE_SOTA, foundedness_strategy_used = FoundednessStrategy.HEURISTIC,
        sota_grounder_path = "./"
        ):

        self.grounding_strategy = grounding_strategy
        self.rule_dictionary = rule_dictionary
        self.facts = facts
        self.query = query
        self.ground_and_solve = ground_and_solve
        self.cyclic_strategy_used = cyclic_strategy_used
        self.foundedness_strategy_used = foundedness_strategy_used
        self.sota_grounder_path = sota_grounder_path

        self.output_type = output_type
        
        self.graph_ds = graph_ds

        self.debug_mode = debug_mode
        self.enable_lpopt = enable_lpopt
        self.output_printer = output_printer
        self.sota_grounder = sota_grounder

        self.enable_logging = enable_logging
        self.logging_class = logging_class

        self.grounded_program = None

        self.grd_call = 0
        self.total_nagg_calls = 0

        self.final_program_input_to_grounder = ""
        self.full_ground = False


        self.cdnl_data_structure = cdnl_data_structure

    def single_ground_call(self, all_heads, grounding_strategy_enum : GroundingStrategy ):

        if self.grounded_program is None: 
            self.grounded_program = StringASPProgram("\n".join(list(self.facts.keys())))

        if self.enable_logging is True:
            self.logging_class.grounding_strategy = self.grounding_strategy

        if self.sota_grounder == SotaGrounder.GRINGO and self.ground_and_solve is False:
            show_statements = "\n".join([f"#show {key}/{all_heads[key]}." for key in all_heads.keys()] + [f"#show -{key}/{all_heads[key]}." for key in all_heads.keys()])
        else:
            show_statements = ""

        domain_transformer = DomainInferer()
        if len(self.grounding_strategy) > 0:
            # Ground SOTA rules with SOTA (gringo/IDLV):
            sota_rules_string = self.rule_list_to_rule_string(self.grounding_strategy[0]["sota"]) 

            if self.enable_logging is True:
                self.logging_class.sota_used_for_rules += sota_rules_string

            program_input = self.grounded_program.get_string() + "\n" + sota_rules_string + "\n" + show_statements

            if self.output_type == Output.DEFAULT_GROUNDER or self.output_type == Output.BENCHMARK:
                if self.sota_grounder == SotaGrounder.GRINGO:
                    final_string = self.start_sota_grounder(program_input, mode="standard")
                    #final_string += show_statements
                else:
                    final_string = self.start_sota_grounder(program_input, mode="standard")

            elif False: # self.output_type == Output.STRING:
                final_string = self.start_sota_grounder(program_input, mode="smodels")
                self.grounded_program = SmodelsASPProgram(self.grd_call)
                self.grounded_program.preprocess_smodels_program(final_string, domain_transformer)
                gringo_string = self.grounded_program.get_string(insert_flags=True)

        else:
            if self.output_type == Output.DEFAULT_GROUNDER:
                final_string = self.start_sota_grounder(program_input)
            final_string = self.grounded_program.get_string()

        if self.debug_mode is True:
            print("--- FINAL ---") 

        if False: # self.output_type == Output.STRING:
            query_statement = ""
            if len(self.query.keys()) > 0:
                query_statement = list(self.query.keys())[0]
            final_string = gringo_string + "\n" + show_statements + "\n" + query_statement

        if self.output_printer:
            self.output_printer.custom_print(final_string)
        else:
            print(final_string)

    #@profile
    def ground(self):

        # Load c_output_redirector
        base_dir = os.path.dirname(__file__)  # Get the directory of the current script
        so_file = os.path.join(base_dir, so_filename)
        c_output_redirector = CDLL(so_file)
        # Set the return type of open_pipe to our struct
        c_output_redirector.open_pipe.restype = PipeFds

        if self.enable_logging is True:
            self.logging_class.grounding_strategy = self.clone_grounding_strategy(self.grounding_strategy)

        domain_inference_called_at_least_once = False

        if self.grounded_program is None: 
            self.grounded_program = StringASPProgram("\n".join(list(self.facts.keys())))

        # Explicitly invoke garbage collection (I do not need facts anymore) 
        del self.facts
        gc.collect()

        domain_transformer = DomainInferer()

        level_index = 0
        while level_index < len(self.grounding_strategy):

            if domain_transformer.unsat_prg_found is True:
                break

            level = self.grounding_strategy[level_index]
            sota_rules = level["sota"]
            bdg_rules = level["bdg"]

            # If this evaluates to true (further down), special techniques have to be used!
            is_non_tight_bdg_part = False

            if self.debug_mode is True:
                print(f"-- {level_index}: SOTA-RULES: {sota_rules}, BDG-RULES: {bdg_rules}")

            if len(bdg_rules) > 0 and domain_inference_called_at_least_once is True:

                #domain_transformer.update_domain_sizes()
                tmp_bdg_old_found_rules = []
                tmp_bdg_new_found_rules = []

                for bdg_rule in bdg_rules:
                    rule = self.rule_dictionary[bdg_rule]

                    if rule.is_tight is False:
                        is_non_tight_bdg_part = True

                for bdg_rule in bdg_rules:

                    rule = self.rule_dictionary[bdg_rule]

                    if self.enable_logging is True:
                        self.logging_class.bdg_marked_for_use_rules += str(rule) + "\n"

                    if rule.in_program_rules is True:
                        if self.foundedness_strategy_used == FoundednessStrategy.GUESS or (is_non_tight_bdg_part and self.cyclic_strategy_used==CyclicStrategy.LEVEL_MAPPINGS):
                            tmp_bdg_old_found_rules.append(bdg_rule)
                        elif self.foundedness_strategy_used == FoundednessStrategy.SATURATION or (is_non_tight_bdg_part and self.cyclic_strategy_used==CyclicStrategy.UNFOUND_SET):
                            tmp_bdg_new_found_rules.append(bdg_rule)
                        else: # Heuristic:
                            methods_approximations = []
                            str_rule = str(rule)
                            self.add_approximate_generated_ground_rules_for_non_ground_rule(domain_transformer,
                                rule, str_rule, methods_approximations)
                            methods_approximations.sort(key = lambda x : x[0])
                            used_method = None
                            for _, tmp_method_used, _ in methods_approximations:
                                if "BDG" in tmp_method_used:
                                    used_method = tmp_method_used
                                    break

                            if used_method == "BDG_OLD":
                                tmp_bdg_old_found_rules.append(bdg_rule)
                            else:
                                tmp_bdg_new_found_rules.append(bdg_rule)
                    else:
                        approx_number_rules, used_method, rule_str = self.get_best_method_by_approximated_rule_count(domain_transformer, rule)

                        if used_method == "SOTA":
                            sota_rules.append(bdg_rule)
                        elif used_method == "BDG_OLD" or is_non_tight_bdg_part:
                            tmp_bdg_old_found_rules.append(bdg_rule)
                        else:
                            tmp_bdg_new_found_rules.append(bdg_rule) 

                no_show = True
                ground_guess = True
                # Custom printer keeps result of prototype (NaGG)
                aggregate_mode = AggregateMode.RA
                grounding_mode = GroundingModes.REWRITE_AGGREGATES_GROUND_FULLY

                if len(tmp_bdg_new_found_rules) > 0:
                    program_input = self.rule_list_to_rule_string(tmp_bdg_new_found_rules)

                    self.infer_head_literals_of_bdg(tmp_bdg_new_found_rules)

                    if self.enable_logging is True:
                        self.logging_class.is_bdg_used = True
                        self.logging_class.is_bdg_new_used = True
                        self.logging_class.bdg_used_for_rules += program_input
                        self.logging_class.bdg_new_used_for_rules += program_input

                    input_rules = []
                    for bdg_rule in bdg_rules:
                        input_rules.append(self.rule_dictionary[bdg_rule])

                    start_time = time.time()

                    # Create a tmpfile for stdout redirect.
                    fd, path = tempfile.mkstemp()

                    try:
                        stdout_backup = c_output_redirector.redirect_stdout_to_fd_and_duplicate_and_close(fd)

                        cython_nagg = CythonNagg(domain_transformer, self.graph_ds,
                            nagg_call_number=self.total_nagg_calls, justifiability_type=JustifiabilityType.SATURATION,
                            full_ground = self.full_ground, c_output_redirector = c_output_redirector)
                        cython_nagg.rewrite_rules(input_rules)
                        end_time = time.time()

                        c_output_redirector.call_flush()
                        pipe_write_backup = c_output_redirector.redirect_stdout_to_fd_and_duplicate_and_close(stdout_backup)

                        os.close(pipe_write_backup)
                        f = open(path, "r")
                        output = f.read()

                        self.grounded_program.add_string(cython_nagg.head_guesses_string)

                        f.close()

                        self.grounded_program.add_other_string(output)
                    except Exception as ex:

                        print(ex)
                        raise ex

                    finally:
                        os.remove(path)

                    if self.enable_logging is True:
                        print(f"---> TIME DURATION CYTHON NAGG NEW: {end_time - start_time}", file=sys.stderr)

                    self.total_nagg_calls += 1

                if len(tmp_bdg_old_found_rules) > 0:

                    if is_non_tight_bdg_part is True and self.cyclic_strategy_used == CyclicStrategy.LEVEL_MAPPINGS:
                        ############################
                        # Handle Level-Mappings!   #
                        ############################

                        domain_predicates = []
                        if "_total" in domain_transformer.domain_dictionary:
                            domain = domain_transformer.domain_dictionary["_total"]["terms"][0]
                            for domain_value in domain.keys():
                                domain_predicates.append(f"dom({domain_value}).")

                        # Used for instantiating heads with variables:
                        gen_head_guesses = GenerateHeadGuesses(None, nagg_call_number=self.total_nagg_calls)

                        tmp_rule = self.rule_dictionary[tmp_bdg_old_found_rules[0]]

                        # Assume 0 is head:
                        head_literal = None
                        for literal in tmp_rule.literals:
                            if "FUNCTION" in literal and literal["FUNCTION"].in_head is True:
                                head_literal = literal["FUNCTION"]
                                break

                        scc_index = self.graph_ds.positive_predicate_scc_index[head_literal.name]

                        scc = self.graph_ds.positive_sccs[scc_index]

                        tmp_variable_index_dictionary = {}
                        scc_heads = []
                        scc_heads_2 = []
                        level_mapping_rules = []
                        # For hybrid grounding:
                        non_bdg_scc_rule_indices = []

                        #######################################################################################
                        # Add intermediate/encapsulated rules (those that are introduced by BDG encapsulation)

                        rule_number = 0
                        for bdg_rule_index in tmp_bdg_old_found_rules:
                            bdg_rule = self.rule_dictionary[bdg_rule_index]

                            # Assume 0 is head:
                            tmp_head_literal = None
                            for literal in bdg_rule.literals:
                                if "FUNCTION" in literal and literal["FUNCTION"].in_head is True:
                                    tmp_head_literal = literal["FUNCTION"]
                                    break

                            if tmp_head_literal is not None:
                                variable_index_dict, atom_string_template = gen_head_guesses.get_head_atom_template(tmp_head_literal,
                                    rule_number, encapsulated_head_template=True, variable_index_dict={},
                                    variable_names = True, variable_index_value=len(tmp_variable_index_dictionary)
                                    )
                                variable_index_dict, atom_string_template_not_encapsulated = gen_head_guesses.get_head_atom_template(tmp_head_literal,
                                    rule_number, encapsulated_head_template=False, variable_index_dict=variable_index_dict,
                                    variable_names = True
                                    )

                                level_mappings_string_template = ":-" + atom_string_template + "," + f"not prec({atom_string_template},{atom_string_template_not_encapsulated})."
                                level_mapping_rules.append(level_mappings_string_template)

                                for variable_name in variable_index_dict.keys():
                                    new_variable = f"{variable_name}{variable_index_dict[variable_name]}"
                                    tmp_variable_index_dictionary[new_variable] = variable_index_dict[variable_name]
                                scc_heads.append((atom_string_template,variable_index_dict))

                                # Same but with different variable names (due to the increased index)
                                variable_index_dict, atom_string_template = gen_head_guesses.get_head_atom_template(tmp_head_literal,
                                    rule_number, encapsulated_head_template=True, variable_index_dict={},
                                    variable_names = True, variable_index_value=len(tmp_variable_index_dictionary)
                                    )
                                for variable_name in variable_index_dict.keys():
                                    new_variable = f"{variable_name}{variable_index_dict[variable_name]}"
                                    tmp_variable_index_dictionary[new_variable] = variable_index_dict[variable_name]
                                scc_heads_2.append((atom_string_template, variable_index_dict))
                        
                            rule_number += 1

                        #######################################################################################
                        # Add all remaining rules (those that were there all the time)
                        for scc_predicate_index in list(scc):
                            rule_indices = self.graph_ds.node_to_rule_lookup[scc_predicate_index]

                            for rule_index in rule_indices:
                                rule = self.rule_dictionary[rule_index]

                                if rule_index not in tmp_bdg_old_found_rules:
                                    non_bdg_scc_rule_indices.append(rule_index)

                                # Assume 0 is head:
                                tmp_head_literal = None
                                for literal in rule.literals:
                                    if "FUNCTION" in literal and literal["FUNCTION"].in_head is True:
                                        tmp_head_literal = literal["FUNCTION"]
                                        break

                                if tmp_head_literal is not None:
                                    variable_index_dict, atom_string_template = gen_head_guesses.get_head_atom_template(tmp_head_literal,
                                        0, encapsulated_head_template=False, variable_index_dict={},
                                        variable_names = True, variable_index_value=len(tmp_variable_index_dictionary)
                                        )
                                    for variable_name in variable_index_dict.keys():
                                        new_variable = f"{variable_name}{variable_index_dict[variable_name]}"
                                        tmp_variable_index_dictionary[new_variable] = variable_index_dict[variable_name]
                                    scc_heads.append((atom_string_template, variable_index_dict))

                                    # Same but with different variable names (due to the increased index)
                                    variable_index_dict, atom_string_template = gen_head_guesses.get_head_atom_template(tmp_head_literal,
                                        0, encapsulated_head_template=False, variable_index_dict={},
                                        variable_names = True, variable_index_value=len(tmp_variable_index_dictionary)
                                        )
                                    for variable_name in variable_index_dict.keys():
                                        new_variable = f"{variable_name}{variable_index_dict[variable_name]}"
                                        tmp_variable_index_dictionary[new_variable] = variable_index_dict[variable_name]
                                    scc_heads_2.append((atom_string_template, variable_index_dict))

                        for scc_head_1_index in range(len(scc_heads)):
                            scc_head_1, scc_head_1_var_dict = scc_heads[scc_head_1_index]
                            for scc_head_2_index in range(scc_head_1_index, len(scc_heads_2)):
                                scc_head_2, scc_head_2_var_dict = scc_heads_2[scc_head_2_index]

                                domains = [f"dom(X{scc_head_1_var_dict[variable]})" for variable in list(scc_head_1_var_dict.keys())]
                                domains += [f"dom(X{scc_head_2_var_dict[variable]})" for variable in list(scc_head_2_var_dict.keys())]

                                level_mapping_rule = "1<={" + f"prec({scc_head_1},{scc_head_2});prec({scc_head_2},{scc_head_1})" + "}<=1" + f" :- {','.join(domains)}."
                                level_mapping_rules.append(level_mapping_rule)
                        level_mapping_rules.append(":-prec(X1,X2),prec(X2,X3),prec(X3,X1),X1!=X2,X1!=X3,X2!=X3.\n")
                        self.grounded_program.add_other_string("\n".join(level_mapping_rules))
                        self.grounded_program.add_other_string("\n".join(domain_predicates) + "\n")


                        for non_bdg_rule_index in non_bdg_scc_rule_indices:
                            if non_bdg_rule_index in sota_rules:
                                non_bdg_rule = self.rule_dictionary[non_bdg_rule_index]
                                
                                # Assume 0 is head:
                                tmp_head_literal = None
                                for literal in non_bdg_rule.literals:
                                    if "FUNCTION" in literal and literal["FUNCTION"].in_head is True:
                                        tmp_head_literal = literal["FUNCTION"]
                                        break

                                new_rule_body = []
                                new_lits = []

                                for literal in non_bdg_rule.literals:
                                    if "FUNCTION" in literal and literal["FUNCTION"].in_head is True:
                                        continue

                                    new_rule_body.append(str(literal["FUNCTION"]))
                                    new_prec = f"prec({str(literal['FUNCTION'])},{str(tmp_head_literal)})"
                                    new_lits.append(new_prec)

                                new_rule_1 = str(tmp_head_literal) + ":-" + ",".join(new_rule_body) + "," + ",".join(new_lits) + "."
                                new_rule_2 = ":-" + ",".join(new_rule_body) + "," + "not " + str(tmp_head_literal) + "."

                                new_rules = new_rule_1 + "\n" + new_rule_2 + "\n"

                                self.rule_dictionary[non_bdg_rule_index] = new_rules

                        ## LEVEL MAPPINGS END ##
                        ########################

                    program_input = self.rule_list_to_rule_string(tmp_bdg_old_found_rules)
                    self.infer_head_literals_of_bdg(tmp_bdg_old_found_rules)

                    if self.enable_logging is True:
                        self.logging_class.is_bdg_used = True
                        self.logging_class.is_bdg_old_used = True
                        self.logging_class.bdg_used_for_rules += program_input
                        self.logging_class.bdg_old_used_for_rules += program_input


                    input_rules = []
                    for bdg_rule in bdg_rules:
                        input_rules.append(self.rule_dictionary[bdg_rule])

                    start_time = time.time()

                    # Create a tmpfile for stdout redirect.
                    fd, path = tempfile.mkstemp()

                    try:
                        stdout_backup = c_output_redirector.redirect_stdout_to_fd_and_duplicate_and_close(fd)

                        cython_nagg = CythonNagg(domain_transformer, self.graph_ds,
                            nagg_call_number=self.total_nagg_calls, justifiability_type=JustifiabilityType.UNFOUND,
                            full_ground = self.full_ground, c_output_redirector = c_output_redirector,
                            is_non_tight_bdg_part=is_non_tight_bdg_part, cyclic_strategy_used=self.cyclic_strategy_used,
                            )
                        cython_nagg.rewrite_rules(input_rules)
                        end_time = time.time()

                        c_output_redirector.call_flush()
                        pipe_write_backup = c_output_redirector.redirect_stdout_to_fd_and_duplicate_and_close(stdout_backup)

                        os.close(pipe_write_backup)
                        f = open(path, "r")
                        output = f.read()

                        # TODO --> FIX?    
                        #self.grounded_program.add_string(cython_nagg.head_guesses_string)

                        f.close()

                        self.grounded_program.add_other_string(output)

                    except Exception as ex:

                        print(ex)
                        raise ex

                    finally:
                        os.remove(path)

                    if self.enable_logging is True:
                        print(f"---> TIME DURATION CYTHON NAGG NEW: {end_time - start_time}", file=sys.stderr)

                    self.total_nagg_calls += 1

                    
            if len(sota_rules) > 0 or domain_inference_called_at_least_once is False:

                if len(sota_rules) == 0 and domain_inference_called_at_least_once is False and len(tmp_rule_string) == 0:
                    level_index -= 1

                domain_inference_called_at_least_once = True

                # Ground SOTA rules with SOTA (gringo/IDLV):
                sota_rules_string = self.rule_list_to_rule_string(sota_rules)

                if self.enable_logging is True:
                    self.logging_class.sota_used_for_rules += sota_rules_string

                program_input = self.grounded_program.get_string() + "\n" + sota_rules_string

                other_program_str = self.grounded_program.other_prg_string
                # Explicitly garbage collect stuff
                del self.grounded_program
                gc.collect()

                decoded_string = self.start_sota_grounder(program_input)

                #parse_string(decoded_string, lambda stm: domain_transformer(stm))
                self.grounded_program = SmodelsASPProgram(self.grd_call)
                self.grounded_program.preprocess_smodels_program(decoded_string, domain_transformer)
                # Add non-ground string input:
                self.grounded_program.add_string(program_input)
                self.grounded_program.other_prg_string = other_program_str

                self.grd_call += 1

                if self.debug_mode is True:
                    print("+++++")
                    print(sota_rules)
                    print(sota_rules_string)
                    print("++")
                    print(decoded_string)
                    print(domain_transformer.domain_dictionary)
                    
                # Explicitly garbage collect stuff
                del decoded_string
                gc.collect()

            level_index += 1

        #if self.output_type != Output.STRING:
        #    del domain_transformer.domain_dictionary
        #    domain_transformer = None

        return domain_transformer
        

    def output_grounded_program(self, all_heads, domain_transformer, grounding_strategy_enum : GroundingStrategy ):

        if self.debug_mode is True:
            print("--- FINAL ---")

        if self.sota_grounder == SotaGrounder.GRINGO and self.ground_and_solve is False:
            show_statements = "\n".join([f"#show {key}/{all_heads[key]}." for key in all_heads.keys()] + [f"#show -{key}/{all_heads[key]}." for key in all_heads.keys()])
        else:
            show_statements = ""


        if grounding_strategy_enum == GroundingStrategy.FULL:
            if False: # self.output_type == Output.STRING:

                query_statement = ""
                if len(self.query.keys()) > 0:
                    query_statement = list(self.query.keys())[0]

                input_program = self.grounded_program.get_string(insert_flags=True) + "\n" +\
                    self.grounded_program.other_prg_string + "\n" + show_statements + "\n" + query_statement
                decoded_string = self.start_sota_grounder(input_program, mode="smodels")

                #parse_string(decoded_string, lambda stm: domain_transformer(stm))
                self.grounded_program = SmodelsASPProgram(self.grd_call)
                self.grounded_program.preprocess_smodels_program(decoded_string, domain_transformer, save_smodels_rules=True)

                # To get a unified acceptable string output, we parse it ourselves (but is slow):
                final_program = self.grounded_program.get_string(insert_flags=True, rewrite_smodels_program=True)

            else:
                if self.sota_grounder == SotaGrounder.GRINGO:

                    if self.full_ground is False:
                        input_program = self.grounded_program.get_string(insert_flags=True) + self.grounded_program.other_prg_string + show_statements
                    else:
                        input_program = self.grounded_program.get_string(insert_flags=True) 

                    del self.grounded_program.other_prg_string
                    del show_statements
                    del self.grounded_program.program_string

                    final_program = self.start_sota_grounder(input_program, mode="standard")

                    del input_program

                    if self.full_ground is False:
                        final_program = final_program
                    else:
                        final_program += self.grounded_program.other_prg_string + "\n" + show_statements

                else:
                    input_program = self.grounded_program.other_prg_string + "\n" +\
                        self.grounded_program.get_string(insert_flags=True)
                    final_program = self.start_sota_grounder(input_program, mode="standard")

                    del self.grounded_program
                    del input_program
        else:
            final_program = self.grounded_program.get_string(insert_flags=True) + self.grounded_program.other_prg_string + show_statements


        if self.output_printer:
            self.output_printer.custom_print(final_program)
        else:
            print(final_program)

    def add_approximate_generated_ground_rules_for_non_ground_rule(self, domain_transformer, rule, str_rule, methods_approximations):
        """
        Calls those methods that approximate the number of instantiated rules.
        """

        approximate_sota_rules = ApproximateGeneratedSotaRules(domain_transformer, rule)
       
        approximated_sota_rule_instantiations = approximate_sota_rules.approximate_sota_size()
        methods_approximations.append((approximated_sota_rule_instantiations, "SOTA", str_rule))

        approximated_bdg_rules = ApproximateGeneratedBDGRules(domain_transformer, rule, self.graph_ds, self.rule_dictionary)
        approximated_bdg_new_rule_instantiations, approximated_bdg_old_rule_instantiations = approximated_bdg_rules.approximate_bdg_sizes()

        methods_approximations.append((approximated_bdg_old_rule_instantiations, "BDG_OLD", str_rule))
        methods_approximations.append((approximated_bdg_new_rule_instantiations, "BDG_NEW", str_rule))

        if self.debug_mode is True:
            print("-------------------------")
            print(f"Rule: {str_rule}")
            print(f"SOTA: {approximated_sota_rule_instantiations}")
            print(f"BDG-OLD: {approximated_bdg_old_rule_instantiations}")
            print(f"BDG-NEW: {approximated_bdg_new_rule_instantiations}")
            print("-------------------------")


    def get_best_method_by_approximated_rule_count(self, domain_transformer, rule, str_rule = None):
        """
        Calls approximate instantiated rules helper, and determines best to use grounding method accordingly.
        """

        methods_approximations = []
        if str_rule is None:
            str_rule = str(rule)

        self.add_approximate_generated_ground_rules_for_non_ground_rule(domain_transformer,
            rule, str_rule, methods_approximations)
        
        min_element = min(methods_approximations, key=lambda x: x[0])

        approx_number_rules = min_element[0]
        used_method = min_element[1]
        rule_str = min_element[2]

        return approx_number_rules, used_method, rule_str


    def rule_list_to_rule_string(self, rules):
        program_input = "\n"
        for rule in rules:
            if rule in self.rule_dictionary:
                program_input += f"{str(self.rule_dictionary[rule])}\n"
            elif isinstance(rule, str):
                program_input += rule
            else:
                print(f"[ERROR] - Could not find rule {rule} in rule-dictionary.")
                raise NotImplementedError() # TBD Fallback

        return program_input

    def infer_head_literals_of_bdg(self, rules):

        for rule_index in rules:

            rule = self.rule_dictionary[rule_index]
            for literal in rule.literals:
                if "FUNCTION" in literal:
                    if literal["FUNCTION"].in_head is True:
                        self.cdnl_data_structure.bdg_literals[literal["FUNCTION"].name] = rule

            


    def start_sota_grounder(self, program_input, timeout=1800, mode="smodels"):

        if self.sota_grounder == SotaGrounder.GRINGO:
            if mode =="smodels":
                output = "--output=smodels"
            elif mode == "standard":
                output = "--output=intermediate"
            else:
                raise NotImplementedError(f"[ERROR] - Mode for grounder (internally) not supported: {mode}")

            arguments = [self.sota_grounder_path, output]

        elif self.sota_grounder == SotaGrounder.IDLV:

            if mode in ["smodels", "standard"]:
                output = "--output=0"
            else:
                raise NotImplementedError(f"[ERROR] - Mode for grounder (internally) not supported: {mode}")

            arguments = [self.sota_grounder_path, output, "--stdin"]

        else:
            raise NotImplementedError(f"Grounder {grounder} not implemented!")

        decoded_string = ""
        try:
            p = subprocess.Popen(arguments, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)       
            (ret_vals_encoded, error_vals_encoded) = p.communicate(input=bytes(program_input, "ascii"), timeout = timeout)

            decoded_string = ret_vals_encoded.decode()
            error_vals_decoded = error_vals_encoded.decode()

            if p.returncode != 0 and p.returncode != 10 and p.returncode != 20 and p.returncode != 30:
                print(f">>>>> Other return code than 0 in helper: {p.returncode}")
                print(error_vals_decoded)
                raise Exception(error_vals_decoded)

        except Exception as ex:
            print(program_input)
            try:
                p.kill()
            except Exception as e:
                pass

            raise Exception(ex) # TBD: Continue if possible

        return decoded_string

    def clone_grounding_strategy(self, grounding_strategy):

        new_grounding_strategy = []

        for item in grounding_strategy:

            tmp_dict = {}
            tmp_dict["sota"] = item["sota"].copy()
            tmp_dict["bdg"] = item["bdg"].copy()
            tmp_dict["lpopt"] = item["lpopt"].copy()
            tmp_dict["dependencies"] = item["dependencies"].copy()

            new_grounding_strategy.append(tmp_dict)

        return new_grounding_strategy
