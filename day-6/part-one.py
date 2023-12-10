with open('day-6/input/input.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

times = [int(time) for time in data[0].split(': ')[1].split()]
distances = [int(time) for time in data[1].split(': ')[1].split()]
race_details = list(zip(times, distances))


race_beat_record = []

for i, race in enumerate(race_details):
    total_time = race[0]
    hold_time = race[0]
    race_beat_record.append(0) # initialize beat record counter per race
    while hold_time > 0:
        race_time = total_time - hold_time
        speed = hold_time
        distance_traveled = speed * race_time
        if distance_traveled > race[1]:
            race_beat_record[i] += 1
        hold_time -= 1

print(race_beat_record[0] * race_beat_record[1] * race_beat_record[2] * race_beat_record[3])


        