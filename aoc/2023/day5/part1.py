with open("sample.txt") as file:
    lines = file.readlines()

content = [g.strip() for g in lines]
seeds, *maps_list = content

seeds = [int(n) for n in seeds.split(":")[1].strip().split(" ")]
maps_list = [l for l in maps_list if l != ""]

ranges = []
temp = []
for i, li in enumerate(maps_list):
    if li[0].isdigit():
        temp.append(list(map(int, li.split())))
    elif len(temp) != 0:
            ranges.append(temp.copy())
            temp.clear()
ranges.append(temp.copy())


new_seeds = []
for rng in ranges:
    t = []
    for dest, src, rl in rng:
        for s in seeds:
            if s in range(src, src + rl):
                new_seeds.append(s - src + dest)
                if s in t:
                    t.remove(s)
                break
            else:
                t.append(s)

    if len(t) != 0:
        for v in t:
            new_seeds.append(v)

    print(new_seeds)
    seeds = new_seeds
    new_seeds.clear()
    t.clear()

print(seeds)
