# Automata-Toolbox

![Descriere imagine](<![Image](https://github.com/user-attachments/assets/eacd5b56-9a68-467c-9ba9-3e4e73e482de)>)

## Overview

This project provides a Python-based framework for simulating various types of automata using configuration files. The system is designed to support four types of automata commonly used in computational theory:

- Deterministic Finite Automata (**DFA**)
- Non-Deterministic Finite Automata (**NFA**)
- Pushdown Automata (**PDA**)
- Context-Free Grammar (**CFG**)

<br>

Each automaton type is configurable via text-based configuration files and can be executed or emulated using this framework. The configuration files follow specific formats and structure, which are parsed and validated to ensure proper automaton behavior.

## Key Features

- **Automaton Simulation**: The system supports both deterministic and non-deterministic finite automata (DFA/NFA), pushdown automata (PDA), and context-free grammar (CFG) parsing.
- **Configuration-based**: Automata are defined using structured configuration files, allowing users to easily describe the components and rules of each automaton.
- **Error Handling**: The framework validates each automaton's configuration and provides meaningful error messages to guide users in correcting invalid inputs.
- **Modular Design**: The code is organized into reusable modules for parsing configuration files, simulating automata, and managing user interactions.

## Usage

<img src="./img/ss1.png" width=35%>

### Generating Templates

To create a template configuration file for an automaton, run the program and select the option for generating a template. The file will be created in the /cfg/ directory.

```
python3 main.py
```

### Configuring Automata

Once a template is generated, fill in the required sections in the .cfg file with the appropriate states, symbols, and transitions for your automaton. Each section is clearly labeled, and the format is strict to ensure correct parsing. For example here is a CFG example for matching parentheses.

<img src="./img/ss2.png" width=55%>

### Running Automata

You can emulate an automaton by choosing the corresponding option from the main menu. The system will validate the configuration file and, if valid, run the automaton on a provided input string.
