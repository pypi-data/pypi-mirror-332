import os
import argparse
from toolbox import templates

CONFIG_DIR = "config"

def generate_template(automaton_type, file_name):
    """Generează un fișier de configurație pentru un automat specific"""

    # Dacă utilizatorul nu oferă o cale completă, salvăm în `config/`
    if not os.path.isabs(file_name):  
        file_name = os.path.join(CONFIG_DIR, file_name)

    # Creăm folderul `config/` dacă nu există
    os.makedirs(CONFIG_DIR, exist_ok=True)

    # Generăm template-ul
    if automaton_type == "dfa":
        templates.dfa_template_generator(file_name)
    elif automaton_type == "nfa":
        templates.nfa_template_generator(file_name)
    elif automaton_type == "pda":
        templates.pda_template_generator(file_name)
    elif automaton_type == "cfg":
        templates.cfg_template_generator(file_name)
    else:
        print("Tip de automat necunoscut. Folosește: dfa, nfa, pda, cfg.")
        return

    print(f"Template-ul pentru {automaton_type.upper()} a fost generat: {file_name}")

def main():
    parser = argparse.ArgumentParser(description="Toolbox CLI - Generator de fișiere pentru automate")
    parser.add_argument("command", choices=["generate"], help="Comanda de executat")
    parser.add_argument("automaton", choices=["dfa", "nfa", "pda", "cfg"], help="Tipul de automat")
    parser.add_argument("file", help="Numele fișierului (va fi salvat în `config/` dacă nu este o cale absolută)")

    args = parser.parse_args()

    if args.command == "generate":
        generate_template(args.automaton, args.file)

if __name__ == "__main__":
    main()
