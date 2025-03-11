# Automata-Toolbox

![Descriere imagine](https://private-user-images.githubusercontent.com/107889454/420669273-eacd5b56-9a68-467c-9ba9-3e4e73e482de.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE1MjI0NjMsIm5iZiI6MTc0MTUyMjE2MywicGF0aCI6Ii8xMDc4ODk0NTQvNDIwNjY5MjczLWVhY2Q1YjU2LTlhNjgtNDY3Yy05YmE5LTNlNGU3M2U0ODJkZS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMzA5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDMwOVQxMjA5MjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04YTcxNDZlODk1NmU3MjUxYmY2ODE4ODUyYzNmNzAwNjlmOTNiMWMwMDgxZTE0MjNhNmEzZjIxYTRhMzUzYzM2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ce5uiWvmN9Pg1q1db3e3aBYBKMEUMP6ZHvYwAavPIjg)

## Overview

Automata Toolbox is a Python framework designed for simulating various types of automata used in computational theory. It supports the following automata types:

- **Deterministic Finite Automata (DFA)**
- **Non-Deterministic Finite Automata (NFA)**
- **Pushdown Automata (PDA)**
- **Context-Free Grammar (CFG)**

This framework allows users to define and execute automata using structured configuration files or Python classes. It provides utilities for parsing, validation, and simulation of automata, making it an ideal tool for learning and experimentation.

---

## Features

✅ **Full Automata Simulation** - Supports DFA, NFA, PDA, and CFG.
✅ **Structured Configuration** - Automata are defined using `.cfg` configuration files.
✅ **Python API** - Automata can be created and run programmatically.
✅ **Command-Line Interface (CLI)** - Automata can be managed directly from the terminal.
✅ **Extensible and Modular** - Designed to be modified and extended easily.

---

## Installation

Automata Toolbox requires **Python 3.7+**. Install it via pip:

```bash
pip install automata_toolbox
```

Alternatively, you can install it from source:

```bash
git clone https://github.com/Cris24dc/Automata-Toolbox.git
cd Automata-Toolbox
pip install -e .
```

---

## CLI Usage

### **Generate an Automaton Template**

```bash
automata generate dfa config/my_dfa.cfg
```

Supported automaton types: `dfa`, `nfa`, `pda`, `cfg`.

### **Run a DFA on an Input String**

```bash
python3 -m toolbox.main config/my_dfa.cfg abba
```

---

## Using the Python API

### **Creating and Running a DFA**

```python
from toolbox import DFA

dfa = DFA("config/example.cfg")
if dfa.is_valid():
    print("DFA is valid")
    print(dfa.run("abba"))
```

### **Using an NFA**

```python
from toolbox import NFA

nfa = NFA("config/example_nfa.cfg")
if nfa.is_valid():
    print("NFA is valid")
    print(nfa.run("abba"))
```

---

## Configuration Files

Each automaton type requires a `.cfg` file structured as follows:

### **DFA Configuration Example**

```
[Sigma]
a
b
end

[States]
q0
q1
end

[Start]
q0
end

[Final]
q1
end

[Delta]
q0 a q1
q1 b q0
end
```

### **CFG Configuration Example**

```
[Variables]
S
end

[Terminals]
a
b
end

[Rules]
S -> aSb
S -> $
end
```

---

## Development and Contribution

To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-xyz`.
3. Commit changes: `git commit -m "Added feature XYZ"`.
4. Push: `git push origin feature-xyz`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

For any questions or contributions, reach out at **cristianandrei752@gmail.com** or visit the GitHub repository: [Automata Toolbox](https://github.com/Cris24dc/Automata-Toolbox.git).
