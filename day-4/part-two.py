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
    card_matches.append({'winning_numbers': len(match_numbers), 'instances': 0}) 


# winning cards instance assigment
for i, card in enumerate(card_matches):
    for j in range(i, i+card['winning_numbers']):
        if j >= len(card_matches):
            break
        card_matches[j+1]['instances'] += (1 * (card['instances'] + 1))  # instances + original (1)


print(sum([card['instances'] for card in card_matches]) + len(card_matches)) # total instances + total original = 6189740
