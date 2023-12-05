import re

with open('day-3/input/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

PATTERN = '\d+'

# get numbers via regex (x coordinates in object)
numbers_regex_objects = [list(re.finditer(PATTERN, line)) for line in data]

# get gears with coordinates
gear_objects = [[((x,y), char) for x, char in enumerate(line) if char == '*'] for y, line in enumerate(data)]

gear_ratios = {}
for y, line in enumerate(gear_objects):
    # define surroundings (y axis)
    y_start_bound = y-1 if y > 0 else y
    y_end_bound = y+1 if y < len(gear_objects) else y

    # get potential part number values (y axis filter per line)
    potential_numbers = [item for l in numbers_regex_objects[y_start_bound: y_end_bound + 1] for item in l]

    for gear in line:
        # Define surrounding (x axis filter per object)
        x_range = range(gear[0][0]-1, gear[0][0]+1)
        
        i = 0
        ratios = []
        # valid gear ratios definition 
        while (i <= (len(potential_numbers) - 1)):
            # check if gear is within a number's surrounding
            x_range = range(potential_numbers[i].span()[0]-1, potential_numbers[i].span()[1]+1)     
            if gear[0][0] in x_range:
                ratios.append(int(potential_numbers[i].group()))
            i += 1

        # if less than two adjacent part numbers, it won't be stored in dictionary 
        if len(ratios) < 2:
            # continue to next gear
            continue
        else:
            # key will be gear coordinates 'x-y'
            gear_ratios['-'.join([str(gear[0][1]), str(gear[0][0])])] = ratios[0] * ratios[1]

print(sum(gear_ratios.values())) # 84363105
