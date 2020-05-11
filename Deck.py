from itertools import product
from random import shuffle

from Card import Card
from Hand import Hand
from CardTypes import Suit, Rank


class Deck(list):

    def __init__(self):
        super().__init__()
        for suit, rank in list(product(Suit, Rank)):
            self.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        shuffle(self)

    def create_hand(self):
        return Hand(self.pop(0), self.pop(0))
