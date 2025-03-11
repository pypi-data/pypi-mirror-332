from toolbox import parser

class PDA:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sigma = []
        self.gamma = []
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
            self.gamma = parser.get_section_content(content, "Gamma")
            self.states = parser.get_section_content(content, "States")
            self.start = parser.get_section_content(content, "Start")[0]
            self.final = parser.get_section_content(content, "Final")
            self._parse_transitions(parser.get_section_content(content, "Delta"))

    def _parse_transitions(self, delta_rules):
        for rule in delta_rules:
            parts = rule.split()
            if len(parts) != 5:
                continue
            state_from, input_char, stack_top, state_to, stack_replacement = parts
            if (state_from, input_char, stack_top) not in self.delta:
                self.delta[(state_from, input_char, stack_top)] = []
            self.delta[(state_from, input_char, stack_top)].append((state_to, stack_replacement))

    def is_valid(self):
        return bool(self.sigma and self.gamma and self.states and self.start and self.final and self.delta)

    def run(self, input_string):
        stack = ["$"]
        current_states = [(self.start, stack)]
        for char in input_string:
            next_states = []
            for state, stack in current_states:
                if stack:
                    stack_top = stack.pop()
                    if (state, char, stack_top) in self.delta:
                        for next_state, stack_replacement in self.delta[(state, char, stack_top)]:
                            new_stack = stack[:]
                            if stack_replacement != "$":
                                new_stack.extend(reversed(stack_replacement))
                            next_states.append((next_state, new_stack))
            current_states = next_states
        return any(state in self.final and not stack for state, stack in current_states)