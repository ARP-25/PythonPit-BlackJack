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

class Participant:
    """

    """
    def __innit__(self, name):
        """

        """
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        """

        """
        self.hand.append

    def show_hand(self):
        """

        """
        print(f"{self.name}'s hand: ")
        for card in self.hand:
            print(f" {card.symbol} {card.logo}")
    
    def hand_value(self):
        """

        """
        hand_value = sum(card.value for card in self.hand)
            hand_value = sum(card.value for card in self.hand)

        ### Aces will get treated as 1 while: ###
        num_aces = sum(1 for card in self.hand if card.value == 11)       
        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value



def main():
    deck = Deck()
    print(deck.print_cards())
    print(deck.shuffle())
    print(deck.print_cards())



main()

