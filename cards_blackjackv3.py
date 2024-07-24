import random

def initialize_deck():
    """Initializes the deck of cards."""
    deck = {2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16, 11: 4}
    return deck

def deal_card(deck):
    """Returns a random card from the deck and updates the deck."""
    available_cards = [card for card, count in deck.items() if count > 0]
    card = random.choice(available_cards)
    deck[card] -= 1
    return card

def calculate_score(cards):
    """Calculates the score based on the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores and returns the result."""
    if user_score == computer_score:
        return "Draw! Dealer wins."
    elif computer_score == 0:
        return "You lose. Blackjack!"
    elif user_score == 0:
        return "You win! Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Plays a game of Blackjack."""
    user_cards = []
    computer_cards = []
    deck = initialize_deck()
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card(deck))
        computer_cards.append(deal_card(deck))

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"  Your cards: {user_cards}, current score: {user_score}")
        print(f"  Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass, or type 'r' to get the rules: ")
            if should_continue == 'y':
                user_cards.append(deal_card(deck))
                if len(user_cards) == 5 and user_score < 21:
                    is_game_over = True
            elif should_continue == 'r':
                print("""
            =========================
                  BLACKJACK RULES
            =========================

            Objective:
            - The goal of Blackjack is to beat the dealer's hand without going over 21.

            Card Values:
            - Numbered cards are worth their face value.
            - Face cards (King, Queen, Jack) are each worth 10.
            - Aces can be worth 1 or 11, whichever is more advantageous for the player.

            Game Flow:
            1. The player and the dealer are each dealt two cards initially.
            2. The player can see both of their cards, but only one of the dealer's cards.
            3. The player must decide whether to "hit" (draw another card) or "stand" (not draw any more cards).
            4. If the player's hand exceeds 21, they "bust" and lose the game.
            5. If the player stands, the dealer reveals their second card.
            6. The dealer must hit until their hand value is 17 or higher.
            7. If the dealer busts, the player wins. Otherwise, the hands are compared.
            8. The hand with a higher value, without exceeding 21, wins.
            9. If the player and the dealer have the same hand value, it's a draw.
            10. If the player draws five cards and stays under 21, they win.

            =========================
            """)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(deck))
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Initialize first play flag
first_play = True

while True:
    if first_play:
        print("""
        ---------- # ------------------------------------------------------------------
        --------- ##= ------------------------------ WELCOME --------------------------
        -------- ##=== -------------------------- TO BLACKJACK! -----------------------
        ------ ###==#=== --------------------------------------------------------------
        ---- ####===##==== ------------------------------------------------------------
        -- #####====###===== ------      This game was coded by Reef Bendl.       -----
        - #####=====####===== -----      Draw cards from the deck,                -----
        - #####=====####===== -----      Try to score higher than the dealer,     -----
        --- ####=  #  #==== -------      BUT DON'T GO OVER 21!                    -----
        --------- ##= -----------------------------------------------------------------
        ------- ####=== ---------------------------------------------------------------
        """)
        first_play = False

    print("\n")
    play_choice = input("   Do you want to play a game of Blackjack? Type 'y' or 'n', (type 'r' to see the rules): ")
    print("\n")

    if play_choice == 'y':
        play_game()
    elif play_choice == 'n':
        print(" Thank you for playing! Goodbye!")
        break
    elif play_choice == 'r':
        print("""
            =========================
                  BLACKJACK RULES
            =========================

            Objective:
            - The goal of Blackjack is to beat the dealer's hand without going over 21.

            Card Values:
            - Numbered cards are worth their face value.
            - Face cards (King, Queen, Jack) are each worth 10.
            - Aces can be worth 1 or 11, whichever is more advantageous for the player.

            Game Flow:
            1. The player and the dealer are each dealt two cards initially.
            2. The player can see both of their cards, but only one of the dealer's cards.
            3. The player must decide whether to "hit" (draw another card) or "stand" (not draw any more cards).
            4. If the player's hand exceeds 21, they "bust" and lose the game.
            5. If the player stands, the dealer reveals their second card.
            6. The dealer must hit until their hand value is 17 or higher.
            7. If the dealer busts, the player wins. Otherwise, the hands are compared.
            8. The hand with a higher value, without exceeding 21, wins.
            9. If the player and the dealer have the same hand value, it's a draw.
            10. If the player draws five cards and stays under 21, they win.

            =========================

            """)
    else:
        print(" Invalid choice. Please try again.\n")
