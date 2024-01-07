with open("input.txt", "r") as file:
    lines = file.readlines()

content = [g.strip() for g in lines]

total = 0
num_map = {}

for card in content:
    card_num = ""
    win_lst = []
    my_list = []

    buff = ""
    for idx, ch in enumerate(card):
        buff += ch

        all_nums = None
        # parse card num
        if ch == ":":
            for b in buff:
                if b.isdigit():
                    card_num += b

            all_nums = card[idx+1:].strip()

        # parse winning numbers
        w_buff = ""
        my_nums = []
        if all_nums is not None:
            for wi, w in enumerate(all_nums):
                if w == "|":
                    my_nums = all_nums[wi+1:].strip()
                    break

                if w.isdigit():
                    w_buff += w

                if w.isspace() and w_buff.strip() != "":
                    win_lst.append(int(w_buff))
                    w_buff = ""

        # parse my num list
        my_buff = ""
        if my_nums is not None:
            for ni, n in enumerate(my_nums):
                if n.isdigit():
                    my_buff += n

                if n.isspace() and my_buff.strip() != "":
                    my_list.append(int(my_buff))
                    my_buff = ""

                if ni == len(my_nums) - 1:
                    my_list.append(int(my_buff.strip()))


    card_wins = 0
    isfirst = True 
    for my_num in my_list:
        if my_num in win_lst:
            if isfirst:
                card_wins = 1
                isfirst = False
            else:
                card_wins *= 2

    total += card_wins

print(total)



