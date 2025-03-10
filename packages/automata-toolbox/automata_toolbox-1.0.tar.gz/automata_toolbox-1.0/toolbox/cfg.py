import toolbox.parser as parser
import random

def cfg_check():
    file_name = input("Enter the name of the config file: ")  # Get file name from user

    content = parser.load_file_content(file_name)  # Load file content

    if content == None:
        return None
    
    sections = parser.get_section_list(content)  # Get list of sections

    required_sections = ["Variables", "Terminals", "Rules"]
    if sorted(sections) != sorted(required_sections):
        print("Invalid sections")  # Check for required sections
        return

    section_contents = {}
    for section in sections:
        section_contents[section] = parser.get_section_content(content, section)
        if not section_contents[section]:
            print(f"Section '{section}' is empty")  # Check for empty sections
            return
    
    variables = section_contents["Variables"]
    terminals = section_contents["Terminals"]
    rules = section_contents["Rules"]

    for section_name, section_content in section_contents.items():
        if section_name in ["Variables", "Terminals"]:
            for line in section_content:
                if len(line.split()) != 1:
                    print(f"Line '{line}' in section '{section_name}' has more than one element")
                    return
        elif section_name == "Rules":
            for line in section_content:
                if len(line.split()) < 3:
                    print(f"Line '{line}' in section 'Rules' has less than three elements: variable, '->', rule")
                    return
                if "->" not in line:
                    print(f"Line '{line}' in section 'Rules' does not have '->'")
                    return
                variable, rule = line.split("->")
                variable = variable.strip()
                if variable not in variables:
                    print(f"Variable '{variable}' not found in 'Variables' section")
                    return
                
                for element in rule.split("->")[0].strip():
                    if element not in variables and element not in terminals and element != "$":
                        print(f"Element '{element}' not found in 'Variables' or 'Terminals' section")
                        return

    print(f"CFG from \"{file_name}\" is valid")  # Confirm CFG validity
    return variables, terminals, rules

def cfg_generator():
    result = cfg_check()  # Perform CFG check
    if result is None:
        return
    
    variables, terminals, rules = result
    starting_variable = variables[0]
    rules_dict = {}
    for rule in rules:
        variable, rule = rule.split("->")
        variable = variable.strip()
        rule = rule.strip()
        if variable not in rules_dict:
            rules_dict[variable] = []
        rules_dict[variable].append(rule)  # Parse rules

    result = starting_variable

    while any([variable in result for variable in variables]):
        for variable in variables:
            if variable in result:
                rule = random.choice(rules_dict[variable])
                result = result.replace(variable, rule, 1)  # Generate string based on rules
                break
        
    print(result.replace("$", ""))  # Print generated string, replacing epsilon transitions
