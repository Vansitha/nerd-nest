with open("input.txt", "r") as file:
    lines = file.readlines()

content = [g.strip() for g in lines]

total = 0
card_map = {}

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

    card_map[int(card_num)] = [win_lst, my_list]

# part 2

card_occ_list = {}

for i, card in enumerate(card_map):
    if i not in card_occ_list:
        card_occ_list[i] = 1

    wins = card_map[card][0]
    my_list = card_map[card][1]

    wins = sum(num in wins for num in my_list)

    for next_card in range(i + 1, i + wins + 1):
        card_occ_list[next_card] = card_occ_list.get(next_card, 1) + card_occ_list[i]

print(sum(card_occ_list.values()))
