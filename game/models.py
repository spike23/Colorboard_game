from django.db import models


# Create your models here.

class GameData(models.Model):
    players = models.IntegerField()
    squares = models.IntegerField()
    cards = models.IntegerField()
    sequence = models.CharField(max_length=100)
    card_list = models.CharField(max_length=1000)
    result = models.CharField(max_length=100)
