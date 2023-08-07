import random

VALID_SUITS = ("Hearts", "Diamonds", "Clubs", "Spades")
VALID_VALUES = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


class Card:
    def __init__(self, suit, value):
        if suit not in VALID_SUITS:
            raise ValueError("invalid suit")
        if value not in VALID_VALUES:
            raise ValueError("invalid value")
        self.suit = suit
        self.value = value

    def display(self):
        print(f"{self.suit}: {self.value}")


class Deck:
    def __init__(self):
        """Create instance of Deck with all possible cards"""
        self.cards = []
        for suit in VALID_SUITS:
            for value in VALID_VALUES:
                self.cards.append(Card(suit, value))

    def is_full(self):
        """Check if deck contains all cards"""
        return len(self.cards) == 52

    def shuffle(self):
        """shuffle cards"""
        if not self.is_full():
            raise Exception("Deck is not full")
        random.shuffle(self.cards)

    def deal(self):
        """deal card if remaining"""
        if len(self.cards) == 0:
            raise Exception("Deck is empty")
        return self.cards.pop()


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    while True:
        try:
            deck.deal().display()
        except Exception:
            break
