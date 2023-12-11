from math import floor

with open('day-8/input/input.txt', 'r') as file:
    left_right, nodes_data = file.read().split('\n\n')

left_right = list(left_right)
nodes_splited = [node_line.split(' = ') for node_line in nodes_data.split('\n')]
nodes_str, nodes_coords = list(zip(*[(_node[0], tuple(_node[1][1:-1].split(', '))) for _node in nodes_splited]))

left_right_lenght = len(left_right)
current_node = 'AAA'
steps = 0
while current_node != 'ZZZ':
    new_node_index = 0 if left_right[steps - (left_right_lenght * floor(steps / left_right_lenght))] == 'L' else 1
    current_node = nodes_coords[nodes_str.index(current_node)][new_node_index]
    steps += 1
    
print(steps) # 20513
