# An application to pre-sell a limited number of cinema tickets.
def box_office():
    """
    Calls the customer function and loops the ticket selling process
    until all tickets have been sold.

    Parameters:
        None

    Variables:
        tickets (int): Tracks the remaining number of tickets for sale.
        buyers (int): Accumulator used to count the total number of buyers.

    Logic:
        1. Initialize the number of tickets to 20.
        2. Initialize buyers to 0.
        3. Loop while tickets remaining is greater than 0.
        4. Call the customer function and subtract the returned value from tickets.
        5. Add one to buyers after each customer call.
        6. Display the number of remaining tickets after each sale.
        7. Display the total number of buyers once all tickets are sold.

    Return:
        None
    """

    # No more than 20 tickets can be sold total.
    tickets = 10
    # We will count how many buyers there were.
    buyers = 0

    # Repeat until all tickets have been sold.
    while tickets > 0:
        print('Hello, welcome to the pre-sale Box Office!')

        # Call the buyer function. Adjust ticket total and buyer total.
        tickets = tickets - customer(tickets)
        buyers += 1

        # display the number of remaining tickets after their purchase.
        print(f'Enjoy the show! We have {tickets} tickets left!')

    # After all tickets are sold, display the total number of buyers.
    print(f'We had {buyers} people buy tickets. What a day!')


def customer(remaining_tickets):
    """
    Asks the user how many tickets they want and validates the input.

    Parameters:
        remaining_tickets (int): The number of tickets currently available.

    Variables:
        limit (int): Maximum number of tickets a buyer may purchase.
        sold (int): Number of tickets requested by the buyer.

    Logic:
        1. Set the limit to 4 tickets per customer.
        2. Prompt the user to input the number of tickets to buy.
        3. Validate that the input is a number.
        4. Convert the input to an integer.
        5. Validate that the number is more than 0.
        6. Validate that the number is within the limit and the number of
           remaining tickets.
        7. If valid, return the number of tickets sold.
           Otherwise, display an error message and repeat the prompt.

    Return:
        int: The number of tickets the customer purchased.
    """

    # Each buyer can buy up to 4 tickets.
    limit = 4

    # Prompt the user for the desired number of tickets
    while True:
        sold = input('What quantity of tickets do you care to purchase?: ')

        # Validate whether they asked for a number
        if sold.isdigit() == False:
            print("I'm sorry, what was that?")
            continue

        # If it is a number, make sure it isn't zero.
        sold = int(sold)
        if sold < 1:
            print("I'm sorry, what was that?")
            continue

        # Make sure their request is within the limit of four and
        # provide a clearer message when the request exceeds the per-customer limit.
        if sold > limit:
            print('Unfortunately, the limit is four tickets per customer.')

        # Make sure we have that many tickets.
        elif sold > remaining_tickets:
            print('Sorry, we do not have enough tickets!')
            # Return the number of tickets sold to the box office.

        else:
            print(f'Alright, here are {sold} tickets!')
            return sold


if __name__ == "__main__":
    box_office()
