import re

with open('day-3/input/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

PATTERN = '\d+'

# get numbers via regex (x coordinates in object)
numbers_regex_objects = [list(re.finditer(PATTERN, line)) for line in data]

# get symbols with coordinates
symbols_objects = [[((x,y), char) for x, char in enumerate(line) if not char.isalnum() and char != '.'] for y, line in enumerate(data)]

part_numbers = []
for y, line in enumerate(numbers_regex_objects):
    # define surroundings (y axis)
    y_start_bound = y-1 if y > 0 else y
    y_end_bound = y+1 if y < len(numbers_regex_objects) else y

    # get potential symbol values (y axis filter per line)
    potential_symbols = [item[0] for l in symbols_objects[y_start_bound: y_end_bound + 1] for item in l]

    for regex_object in line:
        # Define surrounding (x axis filter per object)
        x_range = range(regex_object.span()[0]-1, regex_object.span()[1]+1)  

        # flag for optimization (reduce iterations)
        part_number_flag = False
        i = 0

        # part number definition 
        while (not part_number_flag) and (i <= (len(potential_symbols) - 1)):
            # check if symbol within number's surrounding
            if potential_symbols[i][0] in x_range:
                part_number_flag = True
                part_numbers.append(int(regex_object.group()))
                break
            i += 1

print(sum(part_numbers)) # 553079
