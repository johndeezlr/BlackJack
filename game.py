from deck import Deck
from player import Player
import random
import time

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.fisher_yates_shuffle()

        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

    def player_turn(self):
        while True:
            print("\nYour hand:")
            self.player.show_hand()
            print("Score:", self.player.calculate_score())

            if self.player.calculate_score() > 21:
                print("You busted!")
                return

            choice = input("Hit or Stand (h/s): ").lower()
            if choice == "h":
                self.player.add_card(self.deck.draw())
            else:
                break

    def dealer_turn(self):
        print("\nDealer's turn...")
        time.sleep(1)

        while self.dealer.calculate_score() < 17:
            self.dealer.add_card(self.deck.draw())
            time.sleep(1)

        print("\nDealer's hand:")
        self.dealer.show_hand()
        print("Dealer Score:", self.dealer.calculate_score())

    def determine_winner(self):
        p = self.player.calculate_score()
        d = self.dealer.calculate_score()

        print("\nFinal Results:")
        print("Player:", p)
        print("Dealer:", d)

        if p > 21:
            print("Dealer wins!")
        elif d > 21:
            print("Player wins!")
        elif p > d:
            print("Player wins!")
        elif d > p:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        print("=== Blackjack ===")
        self.deal_initial_cards()

        print("\nDealer shows:")
        self.dealer.show_hand(hide_first=True)

        self.player_turn()
        if self.player.calculate_score() <= 21:
            self.dealer_turn()

        self.determine_winner()