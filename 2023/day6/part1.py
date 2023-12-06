with open("input.txt") as file:
    content = file.readlines()

content = [list(map(int, g.strip().split(":")[1].strip().split())) for g in content]

times, distances = content

# d = s * t

# hold time = speed
# race time = total time - hold time
# d = hold time * race time
# if cd > ad -> record

win_counts = []
for t, d in zip(times, distances):
    win = 0
    for hold_t in range(t + 1):
        speed = hold_t
        race_t = t - hold_t
        d_travelled = hold_t * race_t
        if d_travelled > d:
            win += 1
    win_counts.append(win)

answer = 1
for num in win_counts:
    answer *= num

print(answer)
