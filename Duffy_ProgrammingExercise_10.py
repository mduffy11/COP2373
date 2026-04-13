import random


# Display the draw input instructions after invalid input.
def display_error_message():
    # Display the invalid input message.
    print("I'm sorry, what was that?")

    # Explain how to enter replacement choices.
    print("Enter card positions 1 through 5 separated by commas or spaces.")

    # Explain how to keep all cards.
    print("Enter 0 or press Enter to keep all cards.")

    # Print a blank line after the message.
    print()


# Prompt the user to choose which cards to replace.
def get_draw_choices():
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
            display_error_message()
            continue

        # Convert the input pieces into integers.
        choices = [int(part) for part in parts]

        # Reject any numbers outside the valid range.
        if not all(1 <= choice <= 5 for choice in choices):
            display_error_message()
            continue

        # Remove duplicates and sort the positions.
        choices = sorted(set(choices))

        # Convert the positions to zero-based indexes.
        return [choice - 1 for choice in choices]


# Convert a card number into a card label.
def format_card(card_num):
    # Store the possible card ranks.
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    # Store the possible card suits.
    suits = ["♣", "♦", "♥", "♠"]

    # Find the rank for the card.
    rank = ranks[card_num % 13]

    # Find the suit for the card.
    suit = suits[card_num // 13]

    # Return the formatted card label.
    return rank + suit


# Display the current hand with card positions.
def display_hand(hand, heading):
    # Display a heading for the hand.
    print(heading)

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

    # Deal the starting five-card hand.
    hand = [deck.deal() for _ in range(5)]

    # Display the starting hand.
    display_hand(hand, "Your hand:")

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
        print(f"Dealing {num_new_cards} new card(s)...")

        # Deal the replacement cards.
        new_cards = [deck.deal() for _ in range(num_new_cards)]

        # Build the final hand with kept cards first and new cards at the end.
        hand = kept_cards + new_cards

    # Display a message if no cards were replaced.
    else:
        print("Keeping all cards.")

    # Display the final hand.
    display_hand(hand, "Final hand:")

    # Move the draw discards into the discard pile.
    deck.discards_list.extend(draw_discards)

    # Move the finished hand into the discard pile.
    deck.discards_list.extend(hand)

    # Display the deck status after the round.
    print(f"Cards remaining in deck: {len(deck.card_list)}")
    print(f"Cards in discard pile: {len(deck.discards_list)}")


# Define the Deck class.
class Deck:

    # Initialize the deck and discard pile.
    def __init__(self):
        # Store a standard 52-card deck as numbers 0 through 51.
        self.card_list = [i for i in range(52)]

        # Store an empty discard pile.
        self.discards_list = []

        # Shuffle the starting deck.
        random.shuffle(self.card_list)

    # Reshuffle the discard pile back into the deck.
    def reshuffle(self):
        # Stop if there are no discarded cards to reshuffle.
        if len(self.discards_list) == 0:
            return

        # Display the reshuffle message.
        print("Reshuffling deck...")
        print()

        # Add the discarded cards back into the deck.
        self.card_list.extend(self.discards_list)

        # Clear the discard pile.
        self.discards_list = []

        # Shuffle the refreshed deck.
        random.shuffle(self.card_list)

    # Deal one card from the deck.
    def deal(self):
        # Reshuffle automatically if the deck is empty.
        if len(self.card_list) == 0:
            self.reshuffle()

        # Remove and return the top card from the deck.
        return self.card_list.pop(0)


# Start the poker draw program.
def main():
    # Create the deck object.
    deck = Deck()

    # Display the opening message.
    print("Poker Draw")

    # Repeat until the user chooses to quit.
    while True:
        # Play one full hand.
        play_hand(deck)

        # Repeat until the user enters a valid menu choice.
        while True:
            # Display the next action menu.
            print("1. Deal a new hand")
            print("2. Reshuffle and deal a new hand")
            print("3. Quit")
            print()

            # Collect the user's menu choice.
            choice = input("What would you like to do next?: ").strip()

            # Deal a new hand if option 1 is chosen.
            if choice == "1":
                print()
                break

            # Reshuffle the deck if option 2 is chosen.
            elif choice == "2":
                print()
                deck.reshuffle()
                break

            # End the program if option 3 is chosen.
            elif choice == "3":
                print()
                print("Goodbye.")
                return

            # Display an error message for an invalid menu choice.
            else:
                print("I'm sorry, what was that?")
                print()


# Call the main function.
main()