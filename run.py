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
            print("The deck is empty.")

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

def ask_player_draw_card(player, deck):
    """
    Prompt the player if they want to draw another card from the deck.

    This function asks the player if they want to draw another card during their turn
    and prompts for a 'yes' or 'no' response. If the player chooses to draw a card ('yes'),
    the function adds a card to the player's hand from the deck.

    Parameters:
    - player (Player): The Player instance representing the current player.
    - deck (Deck): The Deck instance representing the deck of playing cards.

    Returns:
    None
    """
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

def show_winner(player, dealer):
    """
    Determine and display the winner of the round based on the participants' hands.

    This function evaluates the hands of the player and dealer to determine the winner
    of the round. .

    Parameters:
    - player (Player): The Player instance representing the player.
    - dealer (Dealer): The Dealer instance representing the dealer.

    Returns:
    None
    """
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

def show_final_hands(player, dealer):
    """
    Display the final hands and results of a round.

    This function prints the final hands of both the player and the dealer, along
    with their respective hand values. It displays the results of the round, showing
    the winner or indicating a draw.

    Parameters:
    - player (Player): The Player instance representing the player.
    - dealer (Dealer): The Dealer instance representing the dealer.

    Returns:
    None
    """
    print("\nRESULTS:\n")
    print(f"{player.name}'s hand value: {player.hand_value()}")
    player.show_hand()
    print("Dealer's hand value:", dealer.hand_value())
    dealer.show_hand(False)

def start_round(player, dealer, deck):   
    """
    Start a round of the Blackjack game.

    This function initiates a round by shuffling the deck, prompting the player to
    place a bet, dealing initial cards to both the player and dealer, allowing the player
    to draw additional cards, enabling the dealer to draw cards as per the rules,
    showing the final hands, determining the winner, and updating the player's credits.

    Parameters:
    - player (Player): The Player instance representing the player.
    - dealer (Dealer): The Dealer instance representing the dealer.
    - deck (Deck): The Deck instance representing the deck of cards.

    Returns:
    None
    """         
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
    ask_player_draw_card(player, deck)

    # Dealer draws cards
    while dealer.hand_value()<17 and not(player.hand_value()>21):
        dealer.add_card_to_hand(deck.draw_card())

    # Show final hands
    show_final_hands(player, dealer)

    # Show Winner
    show_winner(player, dealer)

def continue_play_option(player):
    """
    Prompt the player for their choice to continue playing or leave the table.

    This function checks the player's remaining credits and prompts them to choose
    whether they want to play another round or leave the table based on their credits.

    Parameters:
    - player (Player): The Player instance representing the player.

    Returns:
    bool: True if the player chooses to continue playing, False if they choose to leave.
    """
    if player.credits>0:
        print(f"\nDo you want to play another round or leave the table with {player.credits} $.\nType play to play or random character to leave.")
        player_choice = input()
        if player_choice == "play":
            return True
        else:
            return False
    else:
        print("You got no money left to play. Start a new game to start again with 1000$.")
        return False

def validate_player_name(name):
    """
    Validate the player's name to ensure it contains only letters and is at most 20 characters long.

    Parameters:
    - name (str): The name input by the player.

    Returns:
    bool: True if the name is valid, False otherwise.
    """
    return bool(re.match(r'^[a-zA-Z]{1,20}$', name))

def run_game():
    """
    Run a round of the blackjack game.

    This function manages the flow of a round of the blackjack game, including initializing the game,
    allowing the player to place a bet, dealing cards to the player and dealer,
    managing the player's turn, managing the dealer's turn, determining the winner of the round,
    and updating the player's credits accordingly.

    The function also allows the player to continue playing more rounds or exit the game.

    Returns:
    None
    """
    first_round = True
    while True:
        # Welcome message, initialize Participants
        if first_round == True:   
            print("\nWelcome to the Black Jack Table. You're entering with a total credit of 1000 $.\n")
            while True:
                print("\nUnder which name do you want to be referred to? Please enter below:")
                try:
                    player_name = input()
                    if validate_player_name(player_name):
                        player = Player(player_name)
                        dealer = Dealer("Oscar")
                        break
                    else:
                        raise ValueError("Invalid name. Please enter a valid name with only letters and at most 20 characters.")
                except ValueError as e:
                    print(str(e))

        # Start round    
        deck = Deck()
        start_round(player, dealer, deck)           
        first_round = False

        # Ask Player if he wants to keep playing
        if not continue_play_option(player):
            break

def main():
    run_game()

main()

