import re

with open("input.txt") as file:
    data = file.readlines()

lines = [g.strip() for g in data]

red_cubes = 12
green_cubes = 13
blue_cubes = 14

red = "red"
green = "green"
blue = "blue"

total = 0

for line in lines:
    # Parse the game number
    game_tag = line.split(":")[0]
    game_num = int(game_tag.split(" ")[1])

    # Parse the colors and the count
    colors_line = line.split(":")[1]
    colors_list = re.split(r',|;', colors_line)

    is_valid = True
    for color in colors_list:
        temp = color.strip().split(" ")

        num_cubes = int(temp[0])
        color_word = temp[1]

        if color_word == "red":
            if num_cubes > red_cubes:
                is_valid = False
                break
        if color_word == "blue":
            if num_cubes > blue_cubes:
                is_valid = False
                break
        if color_word == "green":
            if num_cubes > green_cubes:
                is_valid = False
                break

    if is_valid:
        total += game_num

print(total)
