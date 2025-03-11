from toolbox import parser
import random

class CFG:
    def __init__(self, file_path):
        self.file_path = file_path
        self.variables = []
        self.terminals = []
        self.rules = {}
        self._load_config()

    def _load_config(self):
        content = parser.load_file_content(self.file_path)
        if content:
            sections = parser.get_section_list(content)
            self.variables = parser.get_section_content(content, "Variables")
            self.terminals = parser.get_section_content(content, "Terminals")
            self._parse_rules(parser.get_section_content(content, "Rules"))

    def _parse_rules(self, rule_lines):
        for rule in rule_lines:
            if "->" not in rule:
                continue
            variable, production = rule.split("->")
            variable = variable.strip()
            production = production.strip()
            if variable not in self.rules:
                self.rules[variable] = []
            self.rules[variable].append(production)

    def is_valid(self):
        return bool(self.variables and self.terminals and self.rules)

    def generate_string(self):
        if not self.is_valid():
            return None
        result = self.variables[0]
        while any(variable in result for variable in self.variables):
            for variable in self.variables:
                if variable in result:
                    production = random.choice(self.rules[variable])
                    result = result.replace(variable, production, 1)
                    break
        return result.replace("$", "")