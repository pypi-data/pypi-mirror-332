import os
import argparse
from toolbox import templates

CONFIG_DIR = "config"

def generate_template(automaton_type, file_name):
    if not os.path.isabs(file_name):  
        file_name = os.path.join(CONFIG_DIR, file_name)

    os.makedirs(CONFIG_DIR, exist_ok=True)

    if automaton_type == "dfa":
        templates.dfa_template_generator(file_name)
    elif automaton_type == "nfa":
        templates.nfa_template_generator(file_name)
    elif automaton_type == "pda":
        templates.pda_template_generator(file_name)
    elif automaton_type == "cfg":
        templates.cfg_template_generator(file_name)
    else:
        print("Unknown automaton type. Use: dfa, nfa, pda, cfg.")
        return

    print(f"Template for {automaton_type.upper()} has been generated: {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Toolbox CLI - Automaton configuration file generator")
    parser.add_argument("command", choices=["generate"], help="Command to execute")
    parser.add_argument("automaton", choices=["dfa", "nfa", "pda", "cfg"], help="Type of automaton")
    parser.add_argument("file", help="File name (will be saved in `config/` if not an absolute path)")

    args = parser.parse_args()

    if args.command == "generate":
        generate_template(args.automaton, args.file)

if __name__ == "__main__":
    main()
