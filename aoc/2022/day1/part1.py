
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

        largest_calories = max(inventory.values())
        return largest_calories                    

result = find_total()
print(result)
