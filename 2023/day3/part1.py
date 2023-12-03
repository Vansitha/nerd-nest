with open("input.txt") as file:
    lines = file.readlines()

content = [g.strip() for g in lines]

symbols = ['+','-','*','/','=','@','&','%','#','$']

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

        if ch == "." or ch in symbols or idx + 1 == len(curr_line):
            is_valid = False
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
                            is_valid = True
                    if right != None:
                        if prev_line[right] in symbols:
                            is_valid = True
                    if prev_line[middle] in symbols:
                        is_valid = True

                if next_line != None:
                    if left != None:
                        if next_line[left] in symbols:
                            is_valid = True
                    if right != None:
                        if next_line[right] in symbols:
                            is_valid = True
                    if next_line[middle] in symbols:
                        is_valid = True

                # current line left and right 
                if left != None:
                    if curr_line[left] in symbols:
                        is_valid = True

                if right != None:
                    if curr_line[right] in symbols:
                        is_valid = True

            if is_valid:
                print(num_str_buff)
                total += int(num_str_buff)

            num_str_buff = ''
            num_idx_list.clear()

print("==========")
print(total)
