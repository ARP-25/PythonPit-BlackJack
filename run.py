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
        while True:
            try:
                print(f"\nHow much money do you want to bet in this round?\nYou can bet up to {self.credits} $ right now.\n")
                user_input = input("Enter your bet: \n")
                bet = int(user_input)
                if bet < 1 or bet > self.credits:
                    raise ValueError(f"\nInvalid bet. Please enter a positive integer between 1 and {self.credits}.\n")
                
                self.bet = bet
                break
            except ValueError:
                print(f"\nInvalid input. Please enter a valid positive integer between 1 and {self.credits}.\n")

    def round_won(self):
        self.credits += self.bet*2
        print(f"{self.name} has won {self.bet*2} $.\n{self.name} has {self.credits} $ left in the bank.")

    def round_lost(self):
        self.credits -= self.bet
        print(f"{self.name} has lost {self.bet} $.\n{self.name} has {self.credits} $ left in the bank.")

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

def run_game():
    # Enter Game/Black Jack Table
    first_round = True

    while True:
        if first_round == True:   
            print("\nWelcome to the Black Jack Table. You're entering with a total credit of 1000 $.\n")
            print("\nUnder which name do you want to be referred to? Please enter below:")
            player_name = input()
            player = Player(player_name)
            dealer = Dealer("Oscar")
        else:
            print("\nWelcome to the next round at the Black Jack Table.")
            for _ in range(len(player.hand)):
                player.hand.pop()
            for _ in range(len(dealer.hand)):
                dealer.hand.pop()
            
        deck = Deck()
        deck.shuffle()
 
        # Ask to place a bet
        player.place_a_bet()

        # Player and Dealer first two cards
        for _ in range(2):
            player.add_card_to_hand(deck.draw_card())
            dealer.add_card_to_hand(deck.draw_card())

        # Showing the starting Hands
        player.show_hand()
        dealer.show_hand()

        # Ask Player draw card
        while True:
            try:
                draw = input("Do you want to draw another card? (yes/no): ").lower()
                if draw not in ['yes', 'no']:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
                
                if draw == 'yes':
                    player.add_card_to_hand(deck.draw_card())
                    player.show_hand()
                    if player.hand_value() > 21:                
                        break
                elif draw == 'no':
                    break

            except ValueError as e:
                print(str(e) + "\n")

        # Dealer draws cards
        while dealer.hand_value()<17 and not(player.hand_value()>21):
            dealer.add_card_to_hand(deck.draw_card())

        # Show final hands
        print("\nRESULTS:\n")
        print(f"{player.name}'s hand value: {player.hand_value()}")
        player.show_hand()
        print("Dealer's hand value:", dealer.hand_value())
        dealer.show_hand(False)

        # Show Winner
        if dealer.hand_value() > 21:
            print(f"Player: {player.name} won!\n")
            player.round_won()
        elif player.hand_value() > 21:
            print(f"Dealer: {dealer.name} won!\n")
            player.round_lost()
        elif dealer.hand_value()<player.hand_value() and not(player.hand_value()>21):
            print(f"Player: {player.name} won!\n")
            player.round_won()
        elif dealer.hand_value()>player.hand_value() and not(dealer.hand_value()>21):
            print(f"Dealer: {dealer.name} won!\n") 
            player.round_lost()     
        elif dealer.hand_value()==player.hand_value():
            print(f"It's a draw!\n")
        
        first_round = False

        # Ask Player if he wants to keep playing
        if player.credits>0:
            print(f"\nDo you want to play another round or leave the table with {player.credits} $.\nType play to play or random character to leave.")
            player_choice = input()
            if player_choice == "play":
                pass
            else:
                break
        else:
            print("You got no money left to play. Start a new game to start again with 1000$.")
            break

def main():
    run_game()

main()

