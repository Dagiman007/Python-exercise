''' A program that simulates picking a
card from a deck of 52 card '''

from random import shuffle

rank = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suit = ['C','D','H','S']

#shuffle the card
shuffle(rank)
shuffle(suit)

choice = eval(input("Choose a card (1-52): "))

rank_choice = choice % 13
suit_choice = choice % 4

print("you chose ",rank[rank_choice]," of ",suit[suit_choice])

