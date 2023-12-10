#!/bin/zsh

# Check if a day number is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <day-number>"
    exit 1
fi

# Assign the day number to a variable
DAY=$1

# Create the directory structure and files
mkdir -p "day-$DAY/input"
touch "day-$DAY/input/input.txt"
touch "day-$DAY/part-one.py"
touch "day-$DAY/part-two.py"

echo "Created directory and files for day $DAY"