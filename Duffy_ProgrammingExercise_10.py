import random

# Display the invalid input message.
def show_input_error():
    print("I'm sorry, what was that?")
    print("Enter card positions 1 through 5 separated by commas or spaces,")
    print("or enter 0 / press Enter to keep all cards.")
    print()

# Prompt the user to choose which cards to replace.
def get_draw_choices():
    # Repeat until valid input is entered.
    while True:
        # Collect the user's draw choices.
        user_input = input(
            "Enter card positions to replace "
            "(1-5 separated by commas or space, or 0 / Enter to keep all):"
        ).strip()

        #Return an empty list if the user wants to keep all cards.
        if user_input == "" or user_input == "0":
            return []

        # Replace commas with spaces to allpw multiple valid input styles.
        cleaned_input = user_input.replace(",", " ")

        #Split the input into separate pieces.
        parts = cleaned_input.split()

        # CHeck that every piece is a digit.
        if not all(part.isdigit() for part in parts):
            show_input_error()
            continue

        #Convert the input pieces into integers.
        choices = [int(part) for part in parts]

        # Reject any numbers outside the valid range.
        if not all(1 <= choice <= 5 for choice in choices):
            show_input_error()
            continue

        # Remove duplicates and sort the positions
        choices = sorted(set(choices))

        # Convert the positions to zero-based indexes.
        return [choice - 1 for choice in choices]

get_draw_choices()