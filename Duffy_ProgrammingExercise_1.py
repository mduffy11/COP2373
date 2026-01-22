# An application to pre-sell a limited number of cinema tickets.
def box_office():
    # No more than 20 tickets can be sold total.
    tickets = 20
    # We will count how many buyers there were.
    buyers = 0

    # Repeat until all tickets have been sold.
    while tickets > 0:
        print('Hello, welcome to the pre-sale Box Office!')

        #Call the buyer function. Adjust ticket total and buyer total.
        tickets = tickets - customer(tickets)
        buyers += 1

        # display the number of remaining tickets after their purchase.
        print(f'Enjoy the show! We have {tickets} tickets left!')

    # After all tickets are sold, display the total number of buyers.
    print(f'We had {buyers} people buy tickets. What a day!')

def customer(remaining_tickets):
    # Each buyer can buy up to 4 tickets.
    limit = 4

    # Prompt the user for the desired number of tickets
    while True:
        sold = input('How many tickets would you like to buy?: ')

        # Validate whether they asked for a number
        if sold.isdigit() == False:
            print("I'm sorry, what was that?")
            continue

        # If it is a number, make sure it isn't zero.
        sold = int(sold)
        if sold < 1:
            print("I'm sorry, what was that?")
            continue

        # Make sure their request is within the limit of four, and
        # make sure we have that many tickets.
        if sold <= limit and sold <= remaining_tickets:
             print(f'Alright, here are {sold} tickets!')

             # Return the number of tickets sold to the box office.
             return sold
        else:
            print('Sorry, we do not have enough tickets!')

if __name__ == "__main__":
    box_office()