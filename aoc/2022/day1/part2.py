def find_total():
    buffer = []
    inventory = {}
    elf_num = 0

    with open("input.txt", "r") as file:
        for line in file:
            number = line.strip()
            if number.isalnum():
                buffer.append(int(number))
            else:
                total = 0
                for value in buffer:
                    total += value

                elf_num += 1
                inventory[elf_num] = total

                buffer.clear()

    total_values = inventory.values()
    sorted_arr = sorted(total_values, reverse=True)
    first_tree = sorted_arr[:3] 

    t = 0
    for v in first_tree:
        t += v

    return t

result = find_total()
print(result)

