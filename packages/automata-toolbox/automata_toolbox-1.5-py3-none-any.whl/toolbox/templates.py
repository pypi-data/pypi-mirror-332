def dfa_template_generator(file_name):
    file_path = f"{file_name}.cfg"
    content = """[Sigma]\n# Alphabet symbols\nend\n\n[States]\n# DFA states\nend\n\n[Start]\n# Initial state\nend\n\n[Final]\n# Accepting states\nend\n\n[Delta]\n# Transition function\nend"""
    with open(file_path, 'w') as file:
        file.write(content)

def nfa_template_generator(file_name):
    file_path = f"{file_name}.cfg"
    content = """[Sigma]\n# Alphabet symbols\nend\n\n[States]\n# NFA states\nend\n\n[Start]\n# Initial state\nend\n\n[Final]\n# Accepting states\nend\n\n[Delta]\n# Transition function\nend"""
    with open(file_path, 'w') as file:
        file.write(content)

def cfg_template_generator(file_name):
    file_path = f"{file_name}.cfg"
    content = """[Variables]\n# Grammar variables\nend\n\n[Terminals]\n# Terminal symbols\nend\n\n[Rules]\n# Grammar production rules\nend"""
    with open(file_path, 'w') as file:
        file.write(content)

def pda_template_generator(file_name):
    file_path = f"{file_name}.cfg"
    content = """[Sigma]\n# Input alphabet\nend\n\n[Gamma]\n# Stack alphabet\nend\n\n[States]\n# PDA states\nend\n\n[Start]\n# Initial state\nend\n\n[Final]\n# Accepting states\nend\n\n[Delta]\n# Transition function\nend"""
    with open(file_path, 'w') as file:
        file.write(content)
