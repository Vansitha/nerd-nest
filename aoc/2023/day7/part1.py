with open("sample.txt") as file:
    content = file.readlines()

content = [g.strip() for g in content]

# arranged in weakest to strongest
types = [i+1 for i in range(7)]
cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

card_ranks = {c: idx+1 for idx, c in enumerate(cards)}

def find_type(hand):
    hand_chars = list(hand)
    
    labels_map = {}
    for ch in hand_chars:
        if labels_map.get(ch, "") != "":
            labels_map[ch] += 1
            continue
        labels_map[ch] = 1

    # five of a kind
    if len(labels_map) == 1:
        return types[6]
    # four of a kind
    if sorted(labels_map.values()) == [1,4]:
        return types[5]
    # full house
    if sorted(labels_map.values()) == [2,3]:
        return types[4]
    # three of a kind 
    if sorted(labels_map.values()) == [1,1,3]:
        return types[3]
    # two pair
    if sorted(labels_map.values()) == [1,2,2]:
        return types[2]
    # one pair
    if len(labels_map) == 4:
        return types[1]
    # high card
    if len(labels_map) == 5:
        return types[0]

identified_cards = {}
for line in content:
    cards_d, bid = line.split()
    hand_type = find_type(cards_d)

    if identified_cards.get(hand_type, "") != "":
        identified_cards[hand_type].append(cards_d)
        continue

    identified_cards[hand_type] = [cards_d]

def check_card_rank(cl):
    ranked_cards = []
    for i, card_1 in enumerate(cl):
        for card_2 in cl:
            if card_1 != card_2:
                for ch_1, ch_2 in zip(card_1, card_2):
                    if cards.index(ch_1) < cards.index(ch_2):
                        ranked_cards.append(card_1)
                        break
                    elif i == len(cl) - 1:
                        ranked_cards.append(card_1)
                        break

    return ranked_cards

ranks = []
for rank in sorted(identified_cards.keys()):
    cards_lst = identified_cards[rank]

    if len(cards_lst) == 1:
        ranks.append(cards_lst[0])
        continue
    
    type_cards_ranked = check_card_rank(cards_lst)

    for rc in type_cards_ranked:
        ranks.append(rc)

print(ranks)
