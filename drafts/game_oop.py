

class Game:
    def __init__(self, players, sequence, card_list):
        self.players = players
        self.sequence = sequence
        self.card_list = card_list

    def game_result(self,):
        cards_list = [card_symbol for card_symbol in self.card_list.split(',')]
        players = range(1, self.players + 1)
        player_position = {x: -1 for x in players}
        for index, player, cards in self.deck_generator(players, cards_list):
            for card in cards:
                position = player_position[player]
                find_character_substr = self.sequence.find(card, position + 1)
                if find_character_substr < 0 or find_character_substr == len(self.sequence) - 1:
                    print('Player {0} won after {1} cards.'.format(player, index + 1))
                    return 'Player {0} won after {1} cards.'.format(player, index + 1)
                player_position[player] = find_character_substr

        print('No player won after {0} cards.'.format(len(cards_list)))
        return 'No player won after {0} cards.'.format(len(cards_list))

    @staticmethod
    def deck_generator(player, deck):
        player_index = 0
        deck_index = 0
        while deck_index < len(deck):
            if player_index >= len(player):
                player_index = 0

            yield (deck_index, player[player_index], deck[deck_index])

            player_index += 1
            deck_index += 1


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

first = Game(first_input.get('players'), first_input.get('sequence'), first_input.get('card_list'))
second = Game(second_input.get('players'), second_input.get('sequence'), second_input.get('card_list'))
third = Game(third_input.get('players'), third_input.get('sequence'), third_input.get('card_list'))

if __name__ == '__main__':
    first.game_result()
    second.game_result()
    third.game_result()
