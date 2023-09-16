import random

class Card:
    """

    """
    def __init__(self, symbol, value, logo):
        self.symbol = symbol
        self.value = value       
        self.logo = logo

class Deck:
    """

    """
    def __init__(self):
        """

        """
        self.cards = []
        # Creating Card Objects and appending them to Cards List
        for symbol in ["Hearts","Diamonds","Clubs","Spades"]:
            for value in range(2, 11):
                self.cards.append(Card(symbol, value, str(value)))

            for logo in ["Jack","Queen","King"]:
                self.cards.append(Card(symbol, 10, logo))

            self.cards.append(Card(symbol, 11, "Ace"))

    def print_cards(self):
        """

        """
        print(len(self.cards))
        for card in self.cards:
            print(f"Symbol: {card.symbol} Logo: {card.logo}")

    def shuffle(self):
        """

        """
        random.shuffle(self.cards)

    def draw_card(self):
        """

        """
        if len(self.cards>0):
            return self.cards
        else
            print("The deck is empty")


def main():
    deck = Deck()
    print(deck.print_cards())
    print(deck.shuffle())
    print(deck.print_cards())



main()

