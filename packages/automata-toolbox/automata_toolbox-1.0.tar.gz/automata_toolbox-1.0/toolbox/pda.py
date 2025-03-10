import toolbox.parser as parser

def pda_check():
    file_name = input("Please enter a valid filename: ")  # Get file name from user

    content = parser.load_file_content(file_name)  # Load file content

    if content is None:
        return None

    sections = parser.get_section_list(content)  # Get list of sections

    required_sections = ["Sigma", "Gamma", "States", "Start", "Final", "Delta"]
    if sorted(sections) != sorted(required_sections):
        print("Invalid sections")  # Check for required sections
        return

    section_contents = {}
    for section in sections:
        section_contents[section] = parser.get_section_content(content, section)
        if not section_contents[section]:
            print(f"Section '{section}' is empty")  # Check for empty sections
            return

    sigma = section_contents["Sigma"]
    gamma = section_contents["Gamma"]
    states = section_contents["States"]
    start = section_contents["Start"]
    final = section_contents["Final"]
    delta = section_contents["Delta"]

    for section_name, section_content in section_contents.items():
        if section_name in ["Sigma", "Gamma", "States", "Start", "Final"]:
            for line in section_content:
                if len(line.split()) != 1:
                    print(f"Line '{line}' in section '{section_name}' has more than one character")
                    return
        elif section_name == "Delta":
            for line in section_content:
                parts = line.replace(",", "").replace("->", "").split()
                if len(parts) != 5:
                    print(f"Line '{line}' in section 'Delta' has incorrect format")
                    return
                state_from, state_to, input_char, stack_top, stack_replacement = parts
                if state_from not in states:
                    print(f"State '{state_from}' not found in 'States' section")
                    return
                if state_to not in states:
                    print(f"State '{state_to}' not found in 'States' section")
                    return
                if input_char != "$" and input_char not in sigma:
                    print(f"Input character '{input_char}' not found in 'Sigma' section or is not epsilon")
                    return
                if stack_top != "$" and stack_top not in gamma:
                    print(f"Stack top character '{stack_top}' not found in 'Gamma' section or is not epsilon")
                    return
                for char in stack_replacement:
                    if char != "$" and char not in gamma:
                        print(f"Stack replacement character '{char}' not found in 'Gamma' section or is not epsilon")
                        return

    print(f"PDA from \"{file_name}\" is valid")  # Confirm PDA validity

    return sigma, gamma, states, start, final, delta

def pda_emulator():
    result = pda_check()  # Perform PDA check
    if result is None:
        return

    sigma, gamma, states, start, final, delta = result

    string = input("Please enter a string: ")  # Get input string from user

    current_state = start[0]
    stack = []
    transitions = {}

    for line in delta:
        parts = line.replace(",", "").replace("->", "").split()
        state_from, state_to, input_char, stack_top, stack_replacement = parts
        if state_from not in transitions:
            transitions[state_from] = {}
        if input_char not in transitions[state_from]:
            transitions[state_from][input_char] = []
        transitions[state_from][input_char].append((state_to, stack_top, stack_replacement))  # Parse transitions

    def process_transition(transitions, current_state, string, stack):
        # Base case: check if the string is empty, current state is final, and stack is empty
        if not string and current_state in final and not stack:
            return True

        if current_state in transitions:
            # Process epsilon transitions
            if '$' in transitions[current_state]:
                for transition in transitions[current_state]['$']:
                    state_to, stack_top, stack_replacement = transition
                    if stack_top == '$' or (stack and stack[-1] == stack_top):
                        new_stack = stack[:]
                        if stack_top != '$' and new_stack:
                            new_stack.pop()
                        new_stack.extend(stack_replacement[::-1] if stack_replacement != '$' else [])
                        if new_stack and new_stack[-1] == '$':
                            new_stack.pop()
                        if state_to in final and not string and not new_stack:
                            return True
                        if process_transition(transitions, state_to, string, new_stack):
                            return True

            # Process non-epsilon transitions
            if string and string[0] in transitions[current_state]:
                for transition in transitions[current_state][string[0]]:
                    state_to, stack_top, stack_replacement = transition
                    if stack_top == '$' or (stack and stack[-1] == stack_top):
                        new_stack = stack[:]
                        if stack_top != '$' and new_stack:
                            new_stack.pop()
                        new_stack.extend(stack_replacement[::-1] if stack_replacement != '$' else [])
                        if new_stack and new_stack[-1] == '$':
                            new_stack.pop()
                        if state_to in final and len(string) == 1 and not new_stack:
                            return True
                        if process_transition(transitions, state_to, string[1:], new_stack):
                            return True
        return False

    if process_transition(transitions, current_state, string, stack):
        print("String accepted")  # String is accepted if final state is reached
    else:
        print("String rejected")  # String is rejected if final state is not reached
