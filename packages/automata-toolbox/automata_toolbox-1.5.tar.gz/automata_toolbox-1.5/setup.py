from setuptools import setup, find_packages

setup(
    name="automata_toolbox",
    version="1.5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "automata=toolbox.cli:main",
        ],
    },
    description="A Python CLI for DFA, NFA, PDA, and CFG simulation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Andrei Cristian-David",
    author_email="cristianandrei752@gmail.com",
    url="https://github.com/Cris24dc/Automata-Toolbox.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
