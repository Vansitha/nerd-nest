with open("input.txt") as file:
    content = file.readlines()

content = [g.strip().split(":")[1].strip().replace(" ", "") for g in content]
time, distance = map(int, content)

wins = 0
for hold_t in range(time + 1):
    speed = hold_t
    race_t = time - hold_t
    d_travelled = hold_t * race_t
    if d_travelled > distance:
        wins += 1

print(wins)

# d = s * t

# hold time = speed
# race time = total time - hold time
# d = hold time * race time
# if cd > ad -> record

