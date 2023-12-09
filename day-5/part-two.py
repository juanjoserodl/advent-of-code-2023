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
seeds_info = [num for num in numerical_values[0]['seeds'][0]]
new_seeds = list(zip([seed for i, seed in enumerate(seeds_info) if i % 2 == 0],[seed for i, seed in enumerate(seeds_info) if i % 2 != 0]))
seeds_range = [(pair[0], pair[0]+pair[1]) for pair in new_seeds]

# remove seeds from mappings
numerical_values.pop(0)
# keep only mapping values
mappings = [list(mapping.values())[0] for mapping in numerical_values]


min_location_values = []
for seed in seeds_range:
    new_sources = []
    new_sources.append(seed)
    for _map in mappings: 
        new_sources_item = []
        new_sources = list(set(new_sources)) # remove duplicates

        # Help from reddit :) - credits below
        # https://www.youtube.com/watch?v=iqTopXV13LE
        # https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/5.py
        
        for (dest, source, span) in _map: 
            source_end = source + span
            NR = []
            for (item_start, item_end) in new_sources:

                before = (item_start, min(item_end, source))
                overlap = (max(item_start, source) - source + dest, min(item_end, source_end) - source + dest)
                after =  (max(item_start, source_end), item_end)

                if overlap[1]>overlap[0]:
                    new_sources_item.append(overlap)

                if before[1]>before[0]:
                    NR.append(before)
        
                if after[1]>after[0]:
                    NR.append(after)
                
            NR.append((item_start, item_end))
            new_sources = NR
        new_sources = []
        new_sources = new_sources_item
    min_location_values.append(min(new_sources)[0])


print(min(min_location_values)) # 69841803
