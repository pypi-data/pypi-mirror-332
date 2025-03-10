from toolbox import parser

class DFA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sigma = []
        self.states = []
        self.start = None
        self.final = []
        self.delta = {}
        self._load_config()

    def _load_config(self):
        content = parser.load_file_content(self.file_path)
        if content:
            sections = parser.get_section_list(content)
            self.sigma = parser.get_section_content(content, "Sigma")
            self.states = parser.get_section_content(content, "States")
            self.start = parser.get_section_content(content, "Start")[0]
            self.final = parser.get_section_content(content, "Final")
            self._parse_transitions(parser.get_section_content(content, "Delta"))

    def _parse_transitions(self, delta_rules):
        for rule in delta_rules:
            state_from, char, state_to = rule.split()
            if (state_from, char) not in self.delta:
                self.delta[(state_from, char)] = state_to

    def is_valid(self):
        return bool(self.sigma and self.states and self.start and self.final and self.delta)

    def run(self, input_string):
        state = self.start
        for char in input_string:
            if (state, char) in self.delta:
                state = self.delta[(state, char)]
            else:
                return False
        return state in self.final