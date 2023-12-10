from math import sqrt, ceil, floor

with open('day-6/input/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

time = [t for t in data[0].split(': ')[1].split()]
distance = [dist for dist in data[1].split(': ')[1].split()]
race_details = (int(''.join(time)), int(''.join(distance)))

# quadratic formula solution

# x = v * t
#   x = distance = race[1]
#   v = speed = hold_time = (total_time - race_time)
#       total_time = race[0]
#   t = race_time 
# race[1] = (total_time - race_time) * race_time
# 0 = - race_time**2 + total_time * race_time - race[1]
# 0 = - race_time**2 + race[0] * race_time - race[1]
 
result_1 = (-race_details[0] + sqrt(race_details[0]**2 - 4*(-1)*(-race_details[1]))) / (2 * (-1))
result_2 = (-race_details[0] - sqrt(race_details[0]**2 - 4*(-1)*(-race_details[1]))) / (2 * (-1))
print(round(abs(result_2 - result_1))) # 30565288

# brute-force solution

# total_time = race_details[0]
# hold_time = race_details[0]
# race_beat_record = 0
# while hold_time > 0:
#     race_time = total_time - hold_time
#     speed = hold_time
#     distance_traveled = speed * race_time
#     if distance_traveled > race_details[1]:
#         race_beat_record += 1
#     hold_time -= 1
# print(race_beat_record)