# Advent of Code 2015 - in Python

https://adventofcode.com/2015

```bash
# Create venv 
python3 -m venv .venv && echo ".venv" >> .gitignore

# Activate venv
source .venv/bin/activate.fish

# Install stuff
python3 -m pip install -r requirements.txt

# Run all tests
python3 -m unittest discover

# Run specific test
python3 -m unittest tests/test_puzzle_day_01.py

# ... 👨‍💻 ...

# Deactivate venv
deactivate
```
