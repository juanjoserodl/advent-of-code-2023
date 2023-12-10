# Advent of Code 2023

## Overview

This repository contains my personal solutions for the [Advent of Code 2023](https://adventofcode.com/2023) challenges, solved using Python. Advent of Code is an annual set of Christmas-themed programming puzzles that cover a variety of skill sets and challenge types.

## Structure

The repository is structured as follows:

- Each day's challenge is in a separate folder, named `day-xx`, where `xx` is the day number.
- Inside each `day-xx` folder, you'll find:
  - `input/`: A directory containing `input.txt` with the puzzle input.
  - `part-one.py`: The Python script containing the solution for part one.
  - `part-two.py`: The Python script containing the solution for part two.

### Folder Structure Automation

The script `generate-day-folder.sh` is designed to automate the setup for a new day in the "Advent of Code" challenge. When you run this script with a day number as an argument, it creates the day folder and files as follows:

```text
advent-of-code-2023/
└── day-[number]/
    ├── input/
    │   └── input.txt
    ├── part-one.py
    └── part-two.py
```

To use the script:
```bash
chmod +x generate-day-folder.sh  # Make script executable 
bash ./generate-day-folder.sh <day-number>  # Run script with day number
```

## Author

- [Juan José Rodríguez](https://github.com/juanjoserodl)
