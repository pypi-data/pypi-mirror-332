from toolbox import parser

class NFA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sigma = []
        self.states = []
        self.start = []
        self.final = []
        self.delta = {}
        self._load_config()

    def _load_config(self):
        content = parser.load_file_content(self.file_path)
        if content:
            sections = parser.get_section_list(content)
            self.sigma = parser.get_section_content(content, "Sigma")
            self.states = parser.get_section_content(content, "States")
            self.start = parser.get_section_content(content, "Start")
            self.final = parser.get_section_content(content, "Final")
            self._parse_transitions(parser.get_section_content(content, "Delta"))

    def _parse_transitions(self, delta_rules):
        for rule in delta_rules:
            state_from, char, state_to = rule.split()
            if (state_from, char) not in self.delta:
                self.delta[(state_from, char)] = []
            self.delta[(state_from, char)].append(state_to)

    def is_valid(self):
        return bool(self.sigma and self.states and self.start and self.final and self.delta)

    def run(self, input_string):
        current_states = set(self.start)
        for char in input_string:
            next_states = set()
            for state in current_states:
                if (state, char) in self.delta:
                    next_states.update(self.delta[(state, char)])
            current_states = next_states
        return not current_states.isdisjoint(set(self.final))
