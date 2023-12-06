# get input data
with open('day-2/input/input.txt', 'r') as file:
    data_list = [line.strip() for line in file.readlines()]

CUBES_IN_BAG = {'red': 12, 'green': 13, 'blue': 14}

# transform list to dictionary
data_to_dict = {val_list[0].split(' ')[1]: val_list[1].split('; ') for val_list in [val.split(': ') for val in data_list]}

# transform dictionary values: list to dictionary
data_to_dict = {element: [item.split(', ') for item in val] for element, val in data_to_dict.items()  }
data_to_dict = {element: [dict([subitem.split(' ')[::-1]  for subitem in item]) for item in val] for element, val in data_to_dict.items()}

# evaluate each configuration: retrieve max of each color and store only the values in a list per game/id
eval_dict = {
    element: list(
        {
            color: max([int(item[color]) for item in val if color in item.keys()])
            for color in CUBES_IN_BAG.keys()
        }.values()
    )
    for element, val in data_to_dict.items()
}

# get power of set of cubes
eval_filtered = [val[0] * val[1] * val[2] for val in eval_dict.values()]

print(sum(eval_filtered)) # 83707
