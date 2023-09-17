import random

class Card:
    """

    """
    def __init__(self, symbol, value, logo):
        self.symbol = symbol
        self.value = value       
        self.logo = logo

    def __str__(self):
        return f"Card: {self.symbol} {self.logo}"

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
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            print("The deck is empty")

class Participant:
    """

    """
    def __init__(self, name):
        """
        """
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        """

        """
        self.hand.append(card)

    def show_hand(self):
        """

        """
        print(f"\n{self.name}'s hand: ")
        for card in self.hand:
            print(card)
        print("\n")
    
    def hand_value(self):
        """

        """
        hand_value = sum(card.value for card in self.hand)

        ### Aces will get treated as 1 while: ###
        num_aces = sum(1 for card in self.hand if card.value == 11)       
        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value

class Player(Participant):
    def __init__(self, name, bet = 0, credits = 1000):
        """
        """
        self.name = name
        self.hand = []
        self.bet = 0
        self.credits = credits

    def print_credits(self):
        print(f"{self.name} has {self.credits} $.\n")

    def place_a_bet(self):
        max_bet = int(self.credits/2)       
        while True:
            try:
                print(f"How much money do you want to bet in this round?\nYou can bet a total of {max_bet} $")
                user_input = input("Enter your bet: ")
                bet = int(user_input)
                if bet < 1 or bet > max_bet:
                    raise ValueError(f"Invalid bet. Please enter a positive integer between 1 and {max_bet}.")
                
                self.bet = bet
                break
            except ValueError:
                print(f"Invalid input. Please enter a valid positive integer between 1 and {max_bet}.")

    def round_won(self):
        self.credits += self.bet*2
        print(f"{self.name} has won {self.bet*2} $.\n{self.name} has {self.credits} $ left in the bank.")

    def round_lost(self):
        self.credits -= self.bet*2
        print(f"{self.name} has lost {self.bet*2} $.\n{self.name} has {self.credits} $ left in the bank.")

class Dealer(Participant):
    def show_hand(self, first_card_secret = True):
        """

        """
        if first_card_secret == True:
            print(f"{self.name}'s hand: ")
            print("Card: Hidden Card")
            for card in self.hand[1:]:
                print(card)
            print("\n")
        else:
            super().show_hand()

def main():
    """
    ### Test Deck and Card
    deck = Deck()
    print(deck.print_cards())
    
    print(deck.shuffle())
    print(deck.print_cards())
    print(deck.draw_card())
    print(deck.draw_card())
    print("End test Deck,Card and functions\n")

    ### Test Participant
    participant = Participant("Oscar")
    participant.add_card_to_hand(deck.draw_card())
    participant.add_card_to_hand(deck.draw_card())
    print("expected output = participant name and cards value")
    participant.show_hand()
    print(participant.hand_value())
    print("End test Participant Class and functions\n")

    ### Test Player
    player = Player("Henry")
    player.add_card_to_hand(deck.draw_card())
    player.add_card_to_hand(deck.draw_card())
    print("expected output = player name and cards value")
    player.show_hand()
    print(player.hand_value())
    print("End test Player Class and functions\n")

    ### Test Dealer
    dealer = Dealer("Del Pierro")
    dealer.add_card_to_hand(deck.draw_card())
    dealer.add_card_to_hand(deck.draw_card())
    print("expected output = player name and cards value but first card hidden")
    dealer.show_hand()
    print(dealer.hand_value())
    print("End test Dealer Class and functions\n")
    """
    ### Test Game

    deck_one = Deck()
    deck_one.shuffle()

    player = Player("Ronaldo")
    dealer = Dealer("Bestdealer")

    # place a bet
    player.place_a_bet()

    # every player gets two cards
    for _ in range(2):
        player.add_card_to_hand(deck_one.draw_card())
        dealer.add_card_to_hand(deck_one.draw_card())

    # showing starting hands
    player.show_hand()
    dealer.show_hand()

    # Player draw card Option
    while True:
        try:
            draw = input("Do you want to draw a card? (yes/no): ").lower()
            if draw not in ['yes', 'no']:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            
            if draw == 'yes':
                player.add_card_to_hand(deck_one.draw_card())
                player.show_hand()
                if player.hand_value() > 21:                
                    break
            elif draw == 'no':
                break

        except ValueError as e:
            print(str(e) + "\n")

    # Dealer draws cards
    while dealer.hand_value()<17 and not(player.hand_value()>21):
        dealer.add_card_to_hand(deck_one.draw_card())

    # Show final hands
    print("\nRESULTS:\n")
    print(f"{player.name}'s hand value: {player.hand_value()}")
    player.show_hand()
    print("Dealer's hand value:", dealer.hand_value())
    dealer.show_hand(False)

    # Show Winner
    if dealer.hand_value() > 21:
        print(f"Player: {player.name} won!")
        player.round_won()
    elif player.hand_value() > 21:
        print(f"Dealer: {dealer.name} won!")
        player.round_lost()
    elif dealer.hand_value()<player.hand_value() and not(player.hand_value()>21):
        print(f"Player: {player.name} won!")
        player.round_won()
    elif dealer.hand_value()>player.hand_value() and not(dealer.hand_value()>21):
        print(f"Dealer: {dealer.name} won!") 
        player.round_lost()     
    elif dealer.hand_value()==player.hand_value():
        print(f"It's a draw!")
    
    ### validate input
    ### add credit class
    ### wrap game test in game function and refactor game function code to make it more readable
    ### finish doc on class and functions
main()

