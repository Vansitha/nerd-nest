with open("input.txt") as file:
    content = file.read().split("\n\n")

seeds, *blocks = content 

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    for a,b,c in ranges:
        print(a,b,c)

    new = []
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c:
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new
    print('yes')

print(min(seeds))
