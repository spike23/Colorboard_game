from django.shortcuts import render, redirect

# Create your views here.
from .forms import GameForm
from .models import GameData, GameTestInput


def index(request):

    test_case = request.GET.get('input')

    first_input = GameTestInput.objects.filter(pk=1).values()[0]
    second_input = GameTestInput.objects.filter(pk=2).values()[0]
    third_input = GameTestInput.objects.filter(pk=3).values()[0]

    if test_case == '1':
        form = GameForm(initial=first_input)
        return render(request, 'index.html', {'form': form})
    elif test_case == '2':
        form = GameForm(initial=second_input)
        return render(request, 'index.html', {'form': form})
    elif test_case == '3':
        form = GameForm(initial=third_input)
        return render(request, 'index.html', {'form': form})
    else:
        form = GameForm()
        return render(request, 'index.html', {'form': form})


def game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            players = form.cleaned_data.get('players')
            squares = form.cleaned_data.get('squares')
            cards = form.cleaned_data.get('cards')
            sequence = form.cleaned_data.get('sequence')
            card_list = form.cleaned_data.get('card_list')

            result = game_result(players, sequence, card_list)

            game = GameData(players=players, squares=squares, cards=cards, sequence=sequence, card_list=card_list,
                            result=result)
            game.save()

            return render(request, 'index.html', {'form': form, 'game': GameData.objects.last()})

    return redirect('index')


# TODO fill in docstring
def game_result(number_of_players, board_sequence, cards_in_deck):
    """

    :param number_of_players:
    :param board_sequence:
    :param cards_in_deck:
    :return:
    """
    cards_list = [card_symbol for card_symbol in cards_in_deck.split(',')]
    players = range(1, number_of_players + 1)
    player_position = {x: -1 for x in players}
    for index, player, cards in deck_generator(players, cards_list):
        for card in cards:
            position = player_position[player]
            find_character_substr = board_sequence.find(card, position + 1)
            if find_character_substr < 0 or find_character_substr == len(board_sequence) - 1:
                return 'Player {0} won after {1} cards.'.format(player, index + 1)
            player_position[player] = find_character_substr

    return 'No player won after {0} cards.'.format(len(cards_list))


# TODO fill in docstring
def deck_generator(player, deck):
    """

    :param player:
    :param deck:
    :return:
    """
    player_index = 0
    deck_index = 0
    while deck_index < len(deck):
        if player_index >= len(player):
            player_index = 0

        yield (deck_index, player[player_index], deck[deck_index])

        player_index += 1
        deck_index += 1
