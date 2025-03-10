import toolbox.parser as parser

def nfa_check():
    file_name = input("Please enter a valid filename: ")  # Get file name from user

    content = parser.load_file_content(file_name)  # Load file content

    if content is None:
        return None
    
    sections = parser.get_section_list(content)  # Get list of sections

    required_sections = ["Sigma", "States", "Start", "Final", "Delta"]
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
    states = section_contents["States"]
    start = section_contents["Start"]
    final = section_contents["Final"]
    delta = section_contents["Delta"]

    for section_name, section_content in section_contents.items():
        if section_name in ["Sigma", "States", "Start", "Final"]:
            for line in section_content:
                if len(line.split()) != 1:
                    print(f"Line '{line}' in section '{section_name}' has more than one character")
                    return
        elif section_name == "Delta":
            for line in section_content:
                if len(line.split()) > 3:
                    print(f"Line '{line}' in section 'Delta' has more than three characters")
                    return
                if len(line.split()) < 3:
                    print(f"Line '{line}' in section 'Delta' has less than three characters")
                    return
                state_from, char, state_to = line.split()
                if state_from not in states:
                    print(f"State '{state_from}' not found in 'States' section")
                    return
                if char not in sigma and char != '$':
                    print(f"Character '{char}' not found in 'Sigma' section")
                    return
                if state_to not in states:
                    print(f"State '{state_to}' not found in 'States' section")
                    return
                
    print(f"NFA from \"{file_name}\" is valid")  # Confirm NFA validity

    return sigma, states, start, final, delta

def nfa_emulator():
    result = nfa_check()  # Perform NFA check
    if result is None:
        return
    
    sigma, states, start, final, delta = result

    string = input("Please enter a string: ")  # Get input string from user

    def parse_delta(delta):
        transitions = {}
        for line in delta:
            parts = line.split()
            state_from, char, state_to = parts[0], parts[1], parts[2]
            if (state_from, char) not in transitions:
                transitions[(state_from, char)] = []
            transitions[(state_from, char)].append(state_to)  # Parse transitions
        return transitions

    def epsilon_closure(states, transitions):
        closure = set(states)
        stack = list(states)
        
        while stack:
            state = stack.pop()
            if (state, '$') in transitions:
                epsilon_states = transitions[(state, '$')]
                for epsilon_state in epsilon_states:
                    if epsilon_state not in closure:
                        closure.add(epsilon_state)
                        stack.append(epsilon_state)  # Find epsilon closure states
        
        return closure

    transitions = parse_delta(delta)

    def process_nfa(start, final, transitions, string):
        current_states = epsilon_closure(set(start), transitions)
        
        for char in string:
            next_states = set()
            for state in current_states:
                if (state, char) in transitions:
                    next_states.update(transitions[(state, char)])
            current_states = epsilon_closure(next_states, transitions)
        
        return not current_states.isdisjoint(final)  # Check if any final states are reached

    if process_nfa(start, final, transitions, string):
        print("String accepted")  # String is accepted if final state is reached
    else:
        print("String rejected")  # String is rejected if final state is not reached
