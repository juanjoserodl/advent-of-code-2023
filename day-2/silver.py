# get input data
with open('day-2/input/input.txt', 'r') as file:
    data_list = [line.strip() for line in file.readlines()]

CUBES_IN_BAG = {'red': 12, 'green': 13, 'blue': 14}

# transform list to dictionary
data_to_dict = {val_list[0].split(' ')[1]: val_list[1].split('; ') for val_list in [val.split(': ') for val in data_list]}

# transform dictionary values: list to dictionary
data_to_dict = {element: [item.split(', ') for item in val] for element, val in data_to_dict.items()  }
data_to_dict = {element: [dict([subitem.split(' ')[::-1]  for subitem in item]) for item in val ] for element, val in data_to_dict.items()}

# evaluate each configuration, all values per subset must be true, all values per game must be true
eval_dict = {
    element: all(
        [
            all([int(item[color]) <= CUBES_IN_BAG[color] for color in item.keys()]) 
            for item in val
        ]
    ) for element, val in data_to_dict.items()
}

# filter true evaluation keys (IDs to integer)
eval_filtered = [int(element) for element, val in eval_dict.items() if val]

print(sum(eval_filtered)) # 2685
