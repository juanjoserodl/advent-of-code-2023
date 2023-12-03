# get input data
with open('day-1/input/input.txt', 'r') as file:
    data_list = [line.strip() for line in file.readlines()]

# get digits from strings
numeric_values = [[char for char in val if char.isnumeric()] for val in data_list]

# get number needed
calibration_values = [int(''.join([num[0], num[-1]])) for num in numeric_values]

# sum all values
print(sum(calibration_values)) # 54708
