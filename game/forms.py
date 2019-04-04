from django import forms

from game.models import GameTestInput


class GameForm(forms.Form):
    players = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Players quantity'}), min_value=1)

    squares = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Squares on the board'}),
        min_value=1)

    cards = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Cards in the deck'}),
        min_value=1)

    sequence = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sequence of characters on the board',
                                      'pattern': '[A-Za-z ]+', 'title': 'Enter characters only, for example: RYGRYB'}))

    card_list = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Cards in the deck', 'pattern': '[A-Za-z ]+',
                   'title': 'Enter characters only, for example: Q,QQ,Q,Q,QQ,Q'}))
