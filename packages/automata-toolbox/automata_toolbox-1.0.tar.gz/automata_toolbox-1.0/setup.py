from setuptools import setup, find_packages

setup(
    name="automata_toolbox",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "automata=toolbox.cli:main",  # Creează comanda automata
        ],
    },
    description="A Python CLI for DFA, NFA, PDA, and CFG simulation",
    author="Numele tau",
    author_email="email@example.com",
    url="https://github.com/user/automata_toolbox",
)
