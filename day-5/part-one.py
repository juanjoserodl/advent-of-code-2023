import re

with open('day-5/input/input.txt', 'r') as file:
    data = file.read()

PATTERN = '\d+'

# data transformation
text_sections = data.split('\n\n')
sections_splited = [section.strip().split(':') for section in text_sections]
sections_to_dict = [{item[0]: item[1].strip().split('\n')} for item in sections_splited]
numerical_values = [{item: [list(map(int, re.findall(PATTERN, l))) for l in val]} for section in sections_to_dict for item, val in section.items()]

# get seeds
seeds = [num for num in numerical_values[0]['seeds'][0]] 
# remove seeds from mappings
numerical_values.pop(0)
# keep only mapping values
mappings = [list(mapping.values())[0] for mapping in numerical_values]

destination_values = []
for seed in seeds:
    value = seed
    for i, mapping in enumerate(mappings):
        # generate ranges
        source_ranges = [range(unit_map[1], unit_map[1]+unit_map[2]) for unit_map in mapping]
        # check if source lies in any of the ranges
        test_value = [value in rng for rng in source_ranges]
        
        # if not range found, continue to next mapping (destination = source)
        if not any(test_value):
            continue

        first_true_index = test_value.index(True)
        # calculate destination value
        value = mapping[first_true_index][0] + (value - mapping[first_true_index][1])

    destination_values.append(value)

print(min(destination_values)) # 177942185
    