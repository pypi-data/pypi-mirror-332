
import os
import sys

from heuristic_splitter.program_structures.rule import Rule
from heuristic_splitter.domain_inferer import DomainInferer

from cython_nagg.cython.generate_function_combination_part import generate_function_combinations_caller
from cython_nagg.cython.generate_comparison_combination_part import generate_comparison_combinations_caller
from cython_nagg.cython.generate_saturation_justification_helper_variables_part import generate_saturation_justification_helper_variables_caller

from cython_nagg.cython.cython_helpers import printf_

class GenerateSaturationJustifiabilityPartPreprocessor:

    def __init__(self, domain : DomainInferer, nagg_call_number = 0, full_ground = False):

        self.domain = domain

        self.full_ground = full_ground

        self.nagg_call_number = nagg_call_number

        self.just_atom_string = "just_{nagg_call_number}"
        self.just_atom_rule_string = "just_{nagg_call_number}_{rule_number}"
        self.just_atom_literal_string = "just_{nagg_call_number}_{rule_number}_{literal_index}"
        self.just_atom_variable_string = "just_{nagg_call_number}_{rule_number}_{variable}({cython_variable_identifier})"

        self.variable_string = "VARIABLE"
        self.function_string = "FUNCTION"
        self.term_string = "TERM"
        self.binary_operation_string = "BINARY_OPERATION"
        self.comparison_string = "COMPARISON"


    def get_string_template_helper(self, argument, string_template, variable_index_dict, variable_index_value, full_ground):

        if self.variable_string in argument:
            # VARIABLE (e.g., X):
            variable = argument[self.variable_string]
            if variable not in variable_index_dict:
                tmp_variable_index_value = variable_index_value
                variable_index_dict[variable] = tmp_variable_index_value
                variable_index_value += 1
            else:
                tmp_variable_index_value = variable_index_dict[variable]

            if full_ground is True:
                string_template += f"%{tmp_variable_index_value}$s"
            else:
                string_template += f"X{tmp_variable_index_value}"

        elif self.function_string in argument:
            # FUNCTION (e.g., p(X)):
            tmp_function = argument[self.function_string]

            variable_index_value, string_template = self.get_just_atom_string_template_helper(
                tmp_function, variable_index_dict=variable_index_dict,
                variable_index_value=variable_index_value, string_template=string_template)

        elif self.term_string in argument:
            # TERM (e.g., 1):
            string_template += argument[self.term_string]

        elif self.binary_operation_string in argument:
            # BINARY_OPERATION (e.g., 1 + 2)
            binary_operation = argument[self.binary_operation_string]

            variable_index_value, string_template = self.get_string_template_helper(
                binary_operation.arguments[0], variable_index_dict=variable_index_dict,
                variable_index_value=variable_index_value, string_template=string_template)

            string_template += binary_operation.operation

            variable_index_value, string_template = self.get_string_template_helper(
                binary_operation.arguments[1], variable_index_dict=variable_index_dict,
                variable_index_value=variable_index_value, string_template=string_template)

        else:
            print(f"[ERROR] - (Just Saturation Part) Unexpected argument in function arguments: {argument} in {function.name}")
            raise NotImplementedError(f"[ERROR] - (Just Saturation Part) Unexpected argument in function arguments: {argument} in {function.name}")

 
        return variable_index_value, string_template


    def get_just_atom_string_template_helper(self, function, variable_index_dict = {}, variable_index_value = 1,
        string_template = "", full_ground = False):

        string_template += function.name
        if len(function.arguments) > 0:

            string_template += "("

            index = 0
            for argument in function.arguments:

                variable_index_value, string_template, = self.get_string_template_helper(
                    argument, string_template,
                    variable_index_dict, variable_index_value, full_ground)

                index += 1
                if index < len(function.arguments):
                        string_template += ","

            string_template += ")"

        return  variable_index_value, string_template


    def get_just_atom_string_template(self, function, rule_number, full_ground, ignore_signum = False):

        variable_index_dict = {} 
        if function.in_head is True:
            # For head-disentangling (for foundedness)
            clone = function.clone()
            clone.name = f"{function.name}_{self.nagg_call_number}_{rule_number}"

            _, string_template = self.get_just_atom_string_template_helper(clone,
                variable_index_dict=variable_index_dict, full_ground=full_ground)

            # Whenever the head does not exist it is justified (actually found).
            if ignore_signum is False:
                string_template = "not " + string_template
            else:
                string_template = string_template

        else:
            _, string_template = self.get_just_atom_string_template_helper(function,
                variable_index_dict=variable_index_dict, full_ground=full_ground)

            if function.signum < 0:
                # If literal whenever B_r^- predicate does not hold, it inches more towards justifiability
                string_template = "not " + string_template

        return variable_index_dict, string_template


    def get_just_comparison_string_template(self, comparison, rule_number, full_ground):

        variable_index_dict = {}
        string_template = ""
        variable_index_value = 1

        variable_index_value, left_string_template = self.get_string_template_helper(
            comparison.arguments[0], variable_index_dict=variable_index_dict,
            string_template=string_template, variable_index_value=variable_index_value,
            full_ground=full_ground
            )

        variable_index_value, right_string_template = self.get_string_template_helper(
            comparison.arguments[1], variable_index_dict=variable_index_dict,
            string_template=string_template, variable_index_value=variable_index_value,
            full_ground=full_ground
            )


        if comparison.signum >= 0:
            string_template = left_string_template + comparison.operator + right_string_template
        else: # Comparison.signum < 0:
            # As IDLV cannot handle "not X1 = X2" --> Becomes "X1 != X2"
            string_template = left_string_template + comparison.negated_operator + right_string_template

        return variable_index_dict, string_template

    def generate_justifiability_part(self, rule: Rule, variable_domain, rule_number, head_variables):

        literal_index = 0

        head_literal_template = None
        head_literal = None
        literal_templates = []

        for literal in rule.literals:

            if self.function_string in literal:
                # FUNCTION (default)
                variable_index_dict, atom_string_template = self.get_just_atom_string_template(literal[self.function_string], rule_number, self.full_ground)

                arguments = literal[self.function_string].arguments
            elif self.comparison_string in literal:
                # COMPARISON
                variable_index_dict, atom_string_template = self.get_just_comparison_string_template(literal[self.comparison_string], rule_number, self.full_ground)

                arguments = literal[self.comparison_string].arguments
            else:
                raise NotImplementedError(f"[ERROR] - Literal type not implemented {literal}")

            if self.function_string in literal and literal[self.function_string].in_head is True:
                # IN HEAD FUNCTION
                full_string_template = self.just_atom_rule_string.format(
                    nagg_call_number=self.nagg_call_number,
                    rule_number = rule_number)

                head_literal_template = full_string_template
                head_literal = literal[self.function_string]

            else:
                literal_template = self.just_atom_literal_string.format(
                    nagg_call_number=self.nagg_call_number,
                    rule_number = rule_number,
                    literal_index = literal_index
                    )
                literal_templates.append(literal_template)
                full_string_template = literal_template

            if len(arguments) > 0:
                variable_strings = []

                variable_domain_lists  = []
                for _ in variable_index_dict.keys():
                    variable_domain_lists.append(0)

                empty_variable_domain_found = False

                for variable in variable_index_dict.keys():
                    position = variable_index_dict[variable]
                    index = position - 1
                    variable_domain_lists[index] = variable_domain[variable]

                    if len(variable_domain[variable]) == 0:
                        empty_variable_domain_found = True


                    if self.full_ground is True:
                        # Ground fully by own procedure
                        variable_template = f"%{position}$s"
                    else:
                        # Let gringo/IDLV ground it
                        variable_template = f"X{position}"

                    variable_strings.append(self.just_atom_variable_string.format(
                        nagg_call_number=self.nagg_call_number,
                        rule_number = rule_number,
                        variable = variable,
                        cython_variable_identifier = variable_template
                    ))

                if empty_variable_domain_found is False:
                    # Everything except the atom at the end
                    full_string_template_reduced = full_string_template + ":-" + ",".join(variable_strings) + ".\n"
                    # Everything 
                    if len(variable_strings) > 0:
                        full_string_template += ":-" + ",".join(variable_strings) + "," + atom_string_template + ".\n"
                    else:
                        full_string_template += ":-" + atom_string_template + ".\n"

                    if self.function_string in literal:
                        if self.full_ground is True:
                            generate_function_combinations_caller(full_string_template, variable_domain_lists)
                        else:
                            printf_(full_string_template.encode('ascii'))

                    elif self.comparison_string in literal:
                        comparison_operator = literal[self.comparison_string].operator
                        is_simple_comparison = literal[self.comparison_string].is_simple_comparison

                        signum = literal[self.comparison_string].signum

                        if self.full_ground is True:
                            generate_comparison_combinations_caller(
                                full_string_template, full_string_template_reduced,
                                variable_domain_lists, comparison_operator, is_simple_comparison, signum
                            )
                        else:
                            printf_(full_string_template.encode('ascii'))

                elif (self.function_string in literal and literal[self.function_string].signum > 0) or (self.comparison_string in literal and literal[self.comparison_string].signum > 0):
                    # If domain is empty then is surely satisfied (and in B_r^+)
                    full_string_template += ".\n"
                    printf_(full_string_template.encode("ascii"))
            else:
                # 0-Ary atom:
                full_string_template += ":-" +  atom_string_template + ".\n"

                printf_(full_string_template.encode("ascii"))

            literal_index += 1

        # HEAD VARIABLES:
        for variable in head_variables:
            # Justifiability saturation only for head-variables:
            saturation_string_list = []
            for domain_value in variable_domain[variable]:

                cur_sat_variable_instantiated =  self.just_atom_variable_string.format(
                    nagg_call_number = self.nagg_call_number,
                    rule_number = rule_number,
                    variable = variable,
                    cython_variable_identifier = domain_value
                )

                saturation_string_list.append(cur_sat_variable_instantiated)

                saturation_string_2 = cur_sat_variable_instantiated +\
                    ":-" + self.just_atom_string.format(nagg_call_number=self.nagg_call_number) + ".\n"

                printf_(saturation_string_2.encode("ascii"))

            if len(saturation_string_list) > 0:
                saturation_string = "|".join(saturation_string_list) + "."
                
                printf_(saturation_string.encode("ascii"))

        # OTHER VARIABLES:
        for variable in variable_domain:
            if variable in head_variables:
                # Skip head variables:
                continue

            other_variable_local_scope = variable

            just_atom_variable_string_helper = "just_h_{nagg_call_number}_{rule_number}_{variable}({cython_variable_identifier})"

            variables_identifiers = []
            variable_domain_lists  = []
            variable_strings = []

            variables_identifiers.append(f"%1$s")
            variable_domain_lists.append(variable_domain[variable])

            index = 2
            for head_variable in sorted(list(head_variables.keys())):

                if self.full_ground is True:
                    variables_identifiers.append(f"%{index}$s")
                    variable_domain_lists.append(variable_domain[head_variable])

                    # index-1 as they are used in printf individually
                    # Shift due to printing technique
                    variable_strings_identifier = f"%{index-1}$s"

                else:
                    variables_identifiers.append(f"X{index}")
                    
                    # But here is no shift!
                    variable_strings_identifier = f"X{index}"

                variable_strings.append(self.just_atom_variable_string.format(
                    nagg_call_number=self.nagg_call_number,
                    rule_number = rule_number,
                    variable = head_variable,
                    cython_variable_identifier = variable_strings_identifier
                ))

                index += 1
 

            if self.full_ground is True:
                guess_rule_start = "1<={"
                if len(list(head_variables.keys())) > 0:
                    guess_rule_end_instantiated = "}<=1:-" + ','.join(variable_strings) + ".\n"
                else:
                    guess_rule_end_instantiated = "}<=1.\n"

                cur_just_atom_variable_string_helper_instantiated =  just_atom_variable_string_helper.format(
                    nagg_call_number = self.nagg_call_number,
                    rule_number = rule_number,
                    variable = variable,
                    cython_variable_identifier = ",".join(variables_identifiers)
                )           
                cur_just_atom_variable_string_instantiated = self.just_atom_variable_string.format(
                    nagg_call_number = self.nagg_call_number,
                    rule_number = rule_number,
                    variable = variable,
                    cython_variable_identifier = "%1$s"
                    )


                guess_rule_choice_template = cur_just_atom_variable_string_helper_instantiated

                generate_saturation_justification_helper_variables_caller(guess_rule_start, guess_rule_choice_template, guess_rule_end_instantiated, variable_domain_lists)
                abstract_rule_template = cur_just_atom_variable_string_instantiated + ":-" + cur_just_atom_variable_string_helper_instantiated + ".\n"
                generate_function_combinations_caller(abstract_rule_template, variable_domain_lists)
            else:
                guess_rule_start = "\n1<={"

                variable_index_dict, atom_string_template = self.get_just_atom_string_template(head_literal, rule_number, self.full_ground, ignore_signum=True)

                new_variables_identifiers = ["%1$s"]

                sorted_by_values_asc = dict(sorted(variable_index_dict.items(), key=lambda item: item[1], reverse=False))

                variable_strings = []

                for key in sorted_by_values_asc:

                    variable_strings_identifier = f"X{sorted_by_values_asc[key]}"
                    new_variables_identifiers.append(variable_strings_identifier)

                    variable_strings.append(self.just_atom_variable_string.format(
                        nagg_call_number=self.nagg_call_number,
                        rule_number = rule_number,
                        variable = key,
                        cython_variable_identifier = variable_strings_identifier
                    ))

                choices = []

                for domain_value in variable_domain_lists[0]:
                    # Replace %1$s with domain value (always position 0 as I defined it this way)
                    new_variables_identifiers[0] = domain_value

                    cur_just_atom_variable_string_helper_instantiated =  just_atom_variable_string_helper.format(
                        nagg_call_number = self.nagg_call_number,
                        rule_number = rule_number,
                        variable = other_variable_local_scope,
                        cython_variable_identifier = ",".join(new_variables_identifiers)
                    )

                    choices.append(cur_just_atom_variable_string_helper_instantiated)

                non_ground_choice_rule = guess_rule_start + ";".join(choices) + "}<=1 :- " + atom_string_template + ".\n"
                printf_(non_ground_choice_rule.encode('ascii'))

                # Replace %1$s with special variable name (not a X<NUMBER>):
                special_variable = "Y"
                new_variables_identifiers[0] = special_variable
                cur_just_atom_variable_string_helper_instantiated =  just_atom_variable_string_helper.format(
                    nagg_call_number = self.nagg_call_number,
                    rule_number = rule_number,
                    variable = other_variable_local_scope,
                    cython_variable_identifier = ",".join(new_variables_identifiers)
                )        
                cur_just_atom_variable_string_instantiated = self.just_atom_variable_string.format(
                    nagg_call_number = self.nagg_call_number,
                    rule_number = rule_number,
                    variable = other_variable_local_scope,
                    cython_variable_identifier = special_variable
                    )

                if len(list(head_variables.keys())) > 0:
                    combined_other_variables_string = ',' + ','.join(variable_strings) + ".\n"
                else:
                    combined_other_variables_string = ".\n"

                abstract_rule_template = cur_just_atom_variable_string_instantiated + ":-" + cur_just_atom_variable_string_helper_instantiated + combined_other_variables_string
                printf_(abstract_rule_template.encode('ascii'))


        sys.stdout.flush()
        justifiability_rule = head_literal_template + ":-" +  ",".join(literal_templates) + "."

        printf_(justifiability_rule.encode("ascii"))

