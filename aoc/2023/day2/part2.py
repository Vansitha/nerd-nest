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

    red_list = []
    blue_list = []
    green_list = []
    for color in colors_list:
        temp = color.strip().split(" ")

        num_cubes = int(temp[0])
        color_word = temp[1]

        if color_word == "red":
            red_list.append(num_cubes)
        if color_word == "blue":
            blue_list.append(num_cubes)
        if color_word == "green":
            green_list.append(num_cubes)


    red_max = max(red_list)
    blue_max = max(blue_list)
    green_max = max(green_list)
    product = red_max * blue_max * green_max
    total += product 

print(total)
