import random
from card import Card

class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = {
        "A": 11,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10
    }

    def __init__(self):
        self.cards = [Card(suit, rank, value)
                      for suit in self.suits
                      for rank, value in self.ranks.items()]

    def fisher_yates_shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw(self):
        return self.cards.pop() if self.cards else None