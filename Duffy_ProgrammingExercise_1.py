# Write an application to pre-sell a limited number of cinema tickets.
def ticket_stand():
    # No more than 20 tickets can be sold total.
    tickets = 20
    buyers = 0
    # Repeat until all tickets have been sold.
    while tickets > 0:
        tickets = tickets - buyer(tickets)
        buyers += 1
        # and then display the number of remaining tickets after their purchase.
        print(f'Enjoy the show! We have {tickets} tickets left!')
    # Then display the total number of buyers.
    print(f'(We had {buyers} buyers buy tickets)')

def buyer(remaining_tickets):
    # Each buyer can buy up to 4 tickets.
    limit = 4
    print('Hello, welcome to the Ticket Stand!')
    # Prompt the user for the desired number of tickets
    while True:
        sold = input('How many tickets would you like to buy?: ')
        if sold.isdigit() == False:
            print("I'm sorry, what was that?")
            continue
        sold = int(sold)
        if sold < 1:
            print("I'm sorry, what was that?")
            continue
        if sold <= limit and sold <= remaining_tickets:
             print(f'Alright, here are {sold} tickets!')
             # Return the number of tickets sold
             return sold
        else:
            print('Sorry, we do not have enough tickets!')

ticket_stand()