class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def calculate_score(self):
        total = sum(card.value for card in self.hand)
        aces = sum(1 for c in self.hand if c.rank == "A")

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    # Insertion Sort (sort by card value)
    def sort_hand(self):
        for i in range(1, len(self.hand)):
            key = self.hand[i]
            j = i - 1
            while j >= 0 and key.value < self.hand[j].value:
                self.hand[j + 1] = self.hand[j]
                j -= 1
            self.hand[j + 1] = key

    # Binary Search for a card value
    def search_card(self, value):
        low, high = 0, len(self.hand) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.hand[mid].value == value:
                return True
            elif self.hand[mid].value < value:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def show_hand(self, hide_first=False):
        if hide_first:
            print("[Hidden Card]")
            for card in self.hand[1:]:
                print(card)
        else:
            for card in self.hand:
                print(card)