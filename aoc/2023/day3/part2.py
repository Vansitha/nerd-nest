with open("sample3.txt") as file:
    lines = file.readlines()

content = [g.strip() for g in lines]

symbols = ["*"]

gear_list = []
total = 0
for i in range(len(content)):
    prev_line = None
    curr_line = content[i]
    next_line = None

    if i - 1 >= 0:
        prev_line = content[i - 1]

    if i + 1 != len(content):
        next_line = content[i + 1]

    num_str_buff = ''
    num_idx_list = []
    for idx, ch in enumerate(curr_line):
        if ch.isdigit():
            num_str_buff += ch
            num_idx_list.append(idx)

        # process number
        if ch == "." or ch in symbols or idx + 1 == len(curr_line):
            is_valid = False
            star_row = None
            star_col = None
            for num_idx in num_idx_list:

                left = None
                middle = num_idx 
                right = None

                if num_idx - 1 != -1:
                    left = num_idx - 1

                if num_idx + 1 != len(curr_line):
                    right = num_idx + 1

                if prev_line != None:
                    if left != None:
                        if prev_line[left] in symbols:
                            star_row = i - 1
                            star_col = left
                            is_valid = True
                    if right != None:
                        if prev_line[right] in symbols:
                            star_row = i - 1
                            star_col = right 
                            is_valid = True
                    if prev_line[middle] in symbols:
                        star_row = i - 1
                        star_col = middle 
                        is_valid = True

                if next_line != None:
                    if left != None:
                        if next_line[left] in symbols:
                            star_row = i + 1
                            star_col = left 
                            is_valid = True
                    if right != None:
                        if next_line[right] in symbols:
                            star_row = i + 1
                            star_col = right 
                            is_valid = True
                    if next_line[middle] in symbols:
                        star_row = i + 1
                        star_col = middle 
                        is_valid = True

                # current line left and right 
                if left != None:
                    if curr_line[left] in symbols:
                        star_row = i
                        star_col = left 
                        is_valid = True

                if right != None:
                    if curr_line[right] in symbols:
                        star_row = i
                        star_col = right 
                        is_valid = True

            if is_valid:
                #print(num_str_buff, f"[{star_row},{star_col}]")
                # [gear, [start_row, star_col]]
                gear_list.append([int(num_str_buff), [star_row, star_col]])

            num_idx_list.clear()
            num_str_buff = ""


# push i to ignore list
ignore_list = []
for i, gear in enumerate(gear_list):
    for x, g in enumerate(gear_list):
        if i == x or x in ignore_list:
            continue
        
        if set(gear[1]) == set(g[1]):
            print(f"{gear[0]} * {g[0]}")
            total += gear[0] * g[0]
            ignore_list.append(i)
            

print("==========")
print(total)
