
deck_1 = []
deck_2 = []

with open('./data') as f:
    for p_no, deck_section in enumerate(f.read().split("\n\n")):
        for line in deck_section.split("\n")[1:]:
            if p_no == 0:
                deck_1.append(int(line))
            else:
                deck_2.append(int(line))

def combat(deck_1, deck_2):
    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if card_1 > card_2:
            deck_1 += [card_1, card_2]
        else:
            deck_2 += [card_2, card_1]

    return deck_1 if len(deck_1) > 0 else deck_2

w_deck = combat(deck_1, deck_2)

print(sum([c*(k+1) for k, c in enumerate(reversed(w_deck))]))