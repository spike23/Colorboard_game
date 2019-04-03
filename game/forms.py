from django import forms

from game.models import GameTestInput


class GameForm(forms.Form):
    players = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Players quantity'}))

    squares = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Squares on the board'}))

    cards = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Cards in the deck'}))

    sequence = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sequence of characters on the board'}))

    card_list = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cards in the deck'}))
