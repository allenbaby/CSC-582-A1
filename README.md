# CSC 582 Assignment #1: Four-Bit Adder

This project will implement an object-oriented four-bit adder in Python using the required assignment structure. Implementation is being completed incrementally through meaningful Git commits.

## Python Version and Setup

Use Python 3. Create and activate a virtual environment, then install the development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Development Commands

Format the source and test directories with Black:

```bash
black source tests
```

Run the pytest suite:

```bash
pytest
```

Generate documentation for the FourBitAdder package:

```bash
pdoc -o doc source.FourBitAdder
```
