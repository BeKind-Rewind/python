# 4.Program to Shuffle Deck of Cards (itertools, random)

import itertools, random

deck = list (itertools.product(range(1,14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))

random.shuffle(deck)

print("Your hand : ")
for i in range(5) :
  print(deck[i][0], "of", deck[i][1])