import re

# get input data
with open('day-1/input/input.txt', 'r') as file:
    data_list = [line.strip() for line in file.readlines()]

NUMBERS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

# get digit with its position in text
numeric_values = {element: [(i, char) for i, char in enumerate(element) if char.isnumeric()] for element in data_list}

# get text matches
text_values_raw = {element: [list(re.finditer(number, element)) for number in NUMBERS.keys() if number in element] for element in data_list }

# get text numbers position in text 
text_values = {}
for element, val in text_values_raw.items():
    # ititialize new list
    text_values[element] = []

    for item in val:
        if len(item) > 1:
            for subitem in item:
                text_values[element].append( ((subitem.span()[0], NUMBERS[subitem.group()])) )
        else:
            text_values[element].append(((item[0].span()[0], NUMBERS[item[0].group()])))

# join digits with text numbers 
numeric_values = {key: numeric_values[key] + text_values[key] for key in text_values.keys()}

# get final number
min_max_number = {}
for element in numeric_values.keys():
    min_max_number[element] = ''

    numeric_values[element].sort(key=lambda x: x[0])
    min_max_number[element] = int(''.join([numeric_values[element][0][1], numeric_values[element][-1][1]]))

# sum all values
print(sum(min_max_number.values())) # 54087

# TODO 
# [ ] Optimize code to avoid using mutiple loops
# [ ] Ideally, solve this without `re` library
# [ ] Use functions