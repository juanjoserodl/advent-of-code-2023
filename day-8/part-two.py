from math import floor, lcm

with open('day-8/input/input.txt', 'r') as file:
    left_right, nodes_data = file.read().split('\n\n')

left_right = list(left_right)
nodes_splited = [node_line.split(' = ') for node_line in nodes_data.split('\n')]
nodes_str, nodes_coords = list(zip(*[(_node[0], tuple(_node[1][1:-1].split(', '))) for _node in nodes_splited]))

left_right_lenght = len(left_right)
current_node_list = [node for node in nodes_str if node.endswith('A')]

steps = [0] * len(current_node_list)
while not all([n.endswith('Z') for n in current_node_list]):
    new_node_index = 0 if left_right[max(steps) - (left_right_lenght * floor(max(steps) / left_right_lenght))] == 'L' else 1
    steps = [step + 1 if not current_node_list[i].endswith('Z') else step for i, step in enumerate(steps)]
    current_node_list = [nodes_coords[nodes_str.index(current_node)][new_node_index] if not current_node.endswith('Z') else current_node for current_node in current_node_list]

print(lcm(*steps)) # 15995167053923
