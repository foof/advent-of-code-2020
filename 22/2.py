
starting_deck_1 = []
starting_deck_2 = []

with open('./data') as f:
    for p_no, deck_section in enumerate(f.read().split("\n\n")):
        for line in deck_section.split("\n")[1:]:
            if p_no == 0:
                starting_deck_1.append(int(line))
            else:
                starting_deck_2.append(int(line))

def combat_recursive(deck_1, deck_2):
    memory = set()
    while len(deck_1) > 0 and len(deck_2) > 0:
        game_state = (tuple(deck_1), tuple(deck_2))
        if game_state in memory:
            # Player 1 wins ROUND due to repeating pattern
            return [1, deck_1]
        memory.add(game_state)

        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)
        if card_1 <= len(deck_1) and card_2 <= len(deck_2):
            winner, _ = combat_recursive(deck_1[:card_1], deck_2[:card_2])
        else:
            winner = 1 if card_1 > card_2 else 2

        if winner == 1:
            deck_1 += [card_1, card_2]
        else:
            deck_2 += [card_2, card_1]

    return [1, deck_1] if len(deck_1) else [2, deck_2]

w_player, w_deck = combat_recursive(starting_deck_1, starting_deck_2)

print(sum([c*(k+1) for k, c in enumerate(reversed(w_deck))]))