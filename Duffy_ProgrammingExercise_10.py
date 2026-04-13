import random


# Prompt the user to choose which cards to replace.
def get_draw_choices():
    # Display the instructions once.
    print("Enter card positions to replace.")
    print("Use 1 through 5 separated by commas or spaces.")
    print("Enter 0 or press Enter to keep all cards.")
    print()

    # Repeat until valid input is entered.
    while True:
        # Collect the user's draw choices.
        user_input = input("Replace cards: ").strip()

        # Return an empty list if the user wants to keep all cards.
        if user_input == "" or user_input == "0":
            return []

        # Replace commas with spaces to allow multiple valid input styles.
        cleaned_input = user_input.replace(",", " ")

        # Split the input into separate pieces.
        parts = cleaned_input.split()

        # Reject input that contains anything other than digits.
        if not all(part.isdigit() for part in parts):
            print("I'm sorry, what was that?")
            continue

        # Convert the input pieces into integers.
        choices = [int(part) for part in parts]

        # Reject any numbers outside the valid range.
        if not all(1 <= choice <= 5 for choice in choices):
            print("I'm sorry, what was that?")
            continue

        # Remove duplicates and sort the positions.
        choices = sorted(set(choices))

        # Convert the positions to zero-based indexes.
        return [choice - 1 for choice in choices]


# Convert a card number into a card label.
def format_card(card_num):
    # Store the possible card ranks.
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Store the possible card suits.
    suits = ['♣', '♦', '♥', '♠']

    # Find the rank for the card.
    rank = ranks[card_num % 13]

    # Find the suit for the card.
    suit = suits[card_num // 13]

    # Return the formatted card label.
    return rank + suit


# Display the current hand with card positions.
def display_hand(hand):
    # Display a heading for the hand.
    print("Your hand:")

    # Display each card with its position number.
    for i in range(len(hand)):
        print(str(i + 1) + ". " + format_card(hand[i]))

    # Print a blank line after the hand.
    print()


# Play one full poker hand.
def play_hand(deck):
    # Store the cards discarded during the draw phase.
    draw_discards = []

    # Display the opening deal message.
    print("Dealing 5 cards...")
    print()

    # Deal the starting five-card hand.
    hand = [deck.deal() for _ in range(5)]

    # Display the starting hand.
    display_hand(hand)

    # Collect the user's draw choices.
    choices = get_draw_choices()

    # Replace cards if the user selected any.
    if choices:
        # Move the selected cards into the draw discard list.
        for index in choices:
            draw_discards.append(hand[index])

        # Keep only the cards that were not selected.
        kept_cards = [hand[i] for i in range(len(hand)) if i not in choices]

        # Count how many new cards must be dealt.
        num_new_cards = len(choices)

        # Display the draw message.
        print()
        print(f"Dealing {num_new_cards} new card(s)...")
        print()

        # Deal the replacement cards.
        new_cards = [deck.deal() for _ in range(num_new_cards)]

        # Build the final hand with kept cards first and new cards at the end.
        hand = kept_cards + new_cards

    # Display a message if no cards were replaced.
    else:
        print()
        print("Keeping all cards.")
        print()

    # Display the final hand.
    print("Final hand:")
    display_hand(hand)

    # Move the draw discards into the discard pile.
    deck.discards_list.extend(draw_discards)

    # Move the finished hand into the discard pile.
    deck.discards_list.extend(hand)

    # Display the deck status after the round.
    print(f"Cards remaining in deck: {len(deck.card_list)}")
    print(f"Cards in discard pile: {len(deck.discards_list)}")
    print()
