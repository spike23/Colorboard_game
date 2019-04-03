

first_input = {
    'players': 2,
    'squares': 8,
    'cards': 13,
    'sequence': 'RYGPBRYGBRPOP',
    'card_list': 'R,B,GG,Y,P,B,P,RR'
}
second_input = {
    'players': 2,
    'squares': 6,
    'cards': 5,
    'sequence': 'RYGRYB',
    'card_list': 'R,YY,G,G,B'
}
third_input = {
    'players': 3,
    'squares': 9,
    'cards': 6,
    'sequence': 'QQQQQQQQQ',
    'card_list': 'Q,QQ,Q,Q,QQ,Q'
}


def game_result(number_ofplayers, board_sequence, cards_in_deck):
    cards_list = [card_symbol for card_symbol in cards_in_deck.split(',')]
    players = range(1, number_ofplayers + 1)
    player_position = {x: -1 for x in players}
    for index, player, cards in deck_generator(players, cards_list):
        for card in cards:
            position = player_position[player]
            find_character_substr = board_sequence.find(card, position + 1)
            if find_character_substr < 0 or find_character_substr == len(board_sequence) - 1:
                print('Player {0} won after {1} cards.'.format(player, index + 1))
                return 'Player {0} won after {1} cards.'.format(player, index + 1)
            player_position[player] = find_character_substr

    print('No player won after {0} cards.'.format(len(cards_list)))
    return 'No player won after {0} cards.'.format(len(cards_list))


def deck_generator(player, deck):
    player_index = 0
    deck_index = 0
    while deck_index < len(deck):
        if player_index >= len(player):
            player_index = 0

        yield (deck_index, player[player_index], deck[deck_index])

        player_index += 1
        deck_index += 1


if __name__ == '__main__':
    game_result(first_input.get('players'), first_input.get('sequence'), first_input.get('card_list'))
    game_result(second_input.get('players'), second_input.get('sequence'), second_input.get('card_list'))
    game_result(third_input.get('players'), third_input.get('sequence'), third_input.get('card_list'))
