import random

class Card:
    """
    Represents a playing card.

    Attributes:
    - symbol (str): The symbol of the card (e.g., Hearts, Diamonds, Clubs, Spades).
    - value (int): The value of the card.
    - logo (str): The logo or identifier of the card (e.g., Ace, King, Queen, numbers).

    Methods:
    - __init__(symbol, value, logo): Initializes a Card instance.
    - __str__(): Returns a string representation of the card.

    """
    def __init__(self, symbol, value, logo):
        """
        Initialize a playing card.

        Parameters:
        - symbol (str): The symbol of the card (e.g., Hearts, Diamonds, Clubs, Spades).
        - value (int): The value of the card.
        - logo (str): The logo or identifier of the card (e.g., Ace, King, Queen, numbers).
        """
        self.symbol = symbol
        self.value = value       
        self.logo = logo

    def __str__(self):
        """
        Return a string representation of the card.

        Returns:
        str: A string describing the card, including its symbol and logo.
        """
        return f"Card: {self.symbol} {self.logo}"

class Deck:
    """
    Represents a deck of playing cards.

    Attributes:
    - cards (list): A list of Card objects representing the deck of cards.

    Methods:
    - __init__(): Initializes a Deck instance with a standard deck of cards.
    - print_cards(): Prints the number of cards in the deck and details of each card.
    - shuffle(): Shuffles the deck of cards.
    - draw_card(): Draws a card from the deck.
    """
    def __init__(self):
        """
        Initialize a deck of playing cards.
        Creates a standard deck of cards.

        The deck is created with 52 cards, including all four symbols and various values.

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
        Print the number of cards in the deck and details of each card.
        """
        print(len(self.cards))
        for card in self.cards:
            print(f"Symbol: {card.symbol} Logo: {card.logo}")

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Draw a card from the deck.

        Returns:
        Card: A Card object representing the drawn card.
        """
        if len(self.cards)>0:
            return self.cards.pop()
        else:
            print("The deck is empty")

class Participant:
    """
    Represents a participant in the blackjack game.

    Attributes:
    - name (str): The name of the participant.
    - hand (list): A list of Card objects representing the participant's hand.

    Methods:
    - __init__(name): Initializes a Participant instance with the given name and an empty hand.
    - add_card_to_hand(card): Adds a Card object to the participant's hand.
    - show_hand(): Displays the participant's hand.
    - hand_value(): Calculates and returns the value of the participant's hand.
    """
    def __init__(self, name):
        """
        Initialize a participant in the blackjack game.

        Parameters:
        - name (str): The name of the participant.
        """
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        """
        Add a Card object to the participant's hand.

        Parameters:
        - card (Card): A Card object to be added to the hand.
        """
        self.hand.append(card)

    def show_hand(self):
        """
        Display the participant's hand.
        """
        print(f"\n{self.name}'s hand: ")
        for card in self.hand:
            print(card)
        print("\n")
    
    def hand_value(self):
        """
        Calculate the value of the participant's hand.

        Returns:
        int: The total value of the participant's hand.
        """
        hand_value = sum(card.value for card in self.hand)

        ### Aces will get treated as 1 while: ###
        num_aces = sum(1 for card in self.hand if card.value == 11)       
        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value

class Player(Participant):
    """
    Represents a player in the blackjack game, inheriting from the Participant class.

    Attributes:
    - name (str): The name of the player.
    - hand (list): A list of Card objects representing the player's hand.
    - bet (int): The bet amount placed by the player.
    - credits (int): The total credits the player has.

    Methods:
    - __init__(name, bet, credits): Initializes a Player instance with the given name, bet, and credits.
    - print_credits(): Prints the current credit balance of the player.
    - place_a_bet(): Prompts the player to place a bet.
    - round_won(): Updates the player's credits after winning a round.
    - round_lost(): Updates the player's credits after losing a round.
    """
    def __init__(self, name, bet = 0, credits = 1000):
        """
        Initialize a player for the blackjack game.

        Parameters:
        - name (str): The name of the player.
        - bet (int, optional): The initial bet amount. Defaults to 0.
        - credits (int, optional): The initial credits of the player. Defaults to 1000.
        """
        self.name = name
        self.hand = []
        self.bet = 0
        self.credits = credits

    def print_credits(self):
        """
        Print the current credit balance of the player.
        """
        print(f"{self.name} has {self.credits} $.\n")

    def place_a_bet(self):      
        """
        Prompt the player to place a bet for the round.

        Validates the input to ensure a valid bet is placed.
        """
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
        """
        Update the player's credits after winning a round.
        """
        self.credits += self.bet*2
        print(f"{self.name} has won {self.bet*2} $.\n{self.name} has {self.credits} $ left in the bank.")

    def round_lost(self):
        """
        Update the player's credits after losing a round.
        """
        self.credits -= self.bet
        print(f"{self.name} has lost {self.bet} $.\n{self.name} has {self.credits} $ left in the bank.")

class Dealer(Participant):
    """
    Represents the dealer in the blackjack game, inheriting from the Participant class.

    Attributes:
    - name (str): The name of the dealer.
    - hand (list): A list of Card objects representing the dealer's hand.

    Methods:
    - show_hand(first_card_secret=True): Displays the dealer's hand.
    """
    def show_hand(self, first_card_secret = True):
        """
        Display the dealer's hand.

        Parameters:
        - first_card_secret (bool, optional): Whether to keep the first card secret or not. Defaults to True.
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
    """
    Run a round of the blackjack game.

    The function manages the flow of a round of the blackjack game, including initializing the game,
    allowing the player to place a bet, dealing cards to the player and dealer,
    managing the player's turn, managing the dealer's turn, determining the winner of the round,
    and updating the player's credits accordingly.

    The function also allows the player to continue playing more rounds or exit the game.

    Returns:
    None
    """
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
### docstrings
main()

