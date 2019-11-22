from django.db import models
from django.forms import ModelForm
import random
# Create your models here.

class Game(models.Model):
    chosen_word = models.CharField(max_length=5)
  
    # choose a fives word
    def set_chosen_word(self):
        word_file = open("static/fives/fives_words.txt")
        words = word_file.readlines()
        position = random.randint(0,len(words))
        chosen_word = words[position]

    def __str__(self):
        return chosen_word


class Guess(models.Model):
    num_shared = models.IntegerField(default=0)
    guess_text = models.CharField(max_length=5)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.guess_text
