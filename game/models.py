from django.db import models


# Create your models here.

class GameData(models.Model):
    players = models.IntegerField()
    squares = models.IntegerField()
    cards = models.IntegerField()
    sequence = models.CharField(max_length=100)
    card_list = models.CharField(max_length=1000)
    result = models.CharField(max_length=100)

    def __str__(self):
        return '{0}{1}{2}{3}{4}{5}'.format(self.players, self.squares, self.cards, self.sequence, self.card_list,
                                           self.result)


class GameTestInput(models.Model):
    players = models.IntegerField()
    squares = models.IntegerField()
    cards = models.IntegerField()
    sequence = models.CharField(max_length=100)
    card_list = models.CharField(max_length=1000)

    def __str__(self):
        return '{0}{1}{2}{3}{4}'.format(self.players, self.squares, self.cards, self.sequence, self.card_list)
