import re

with open('day-4/input/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

PATTERN = '\d+'

splitted_numbers = [line.split(': ')[1].split('|') for line in data]

winner_numbers = [[int(item) for item in re.findall(PATTERN, line[0])] for line in splitted_numbers]
numbers_you_have = [[int(item) for item in re.findall(PATTERN, line[1])] for line in splitted_numbers]

card_matches = []
for i, card in enumerate(numbers_you_have):
    match_numbers = [num for num in card if num in winner_numbers[i]]
    card_matches.append(len(match_numbers))

# doubles after first match
points_per_card = [2**(card-1) if card >=2 else card for card in card_matches]

print(sum(points_per_card))
