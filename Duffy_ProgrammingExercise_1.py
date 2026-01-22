# Write an application to pre-sell a limited number of cinema tickets.
def ticket_stand():
    # No more than 20 tickets can be sold total.
    tickets = 20
    buyers = 0
    # Repeat until all tickets have been sold.
    while tickets > 0:
        buyers += 1
        ticket = tickets - buyer()
    # and then display the number of remaining tickets after their purchase.
    print(tickets)

def buyer():
    # Each buyer can buy up to 4 tickets.
    limit = 4
    print("Hello, welcome to the Ticket Stand!")
    # Prompt the user for the desired number of tickets
    sold = int(input("How many tickets would you like to buy?: "))
    return sold


def sales_report(buyers):
    # Then display the total number of buyers.
    print(buyers)