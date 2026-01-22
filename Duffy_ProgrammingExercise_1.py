# # Write an application to pre-sell a limited number of cinema tickets.
# def ticket_stand():
#     # No more than 20 tickets can be sold total.
#     tickets = 20
#     buyers = 0
#     # Repeat until all tickets have been sold.
#     while tickets > 0:
#         buyers += 1
#         tickets = tickets - buyer()
#         # and then display the number of remaining tickets after their purchase.
#         print(tickets)
#     else:
#         sales_report()

# def sales_report(buyers):
#     # Then display the total number of buyers.
#     print(buyers)

def buyer(remaining_tickets):
    # Each buyer can buy up to 4 tickets.
    limit = 4
    print('Hello, welcome to the Ticket Stand!')
    # Prompt the user for the desired number of tickets
    sold = input('How many tickets would you like to buy?: ')

    while sold.isdigit() == False:
        sold = input("I'm sorry, can you please tell me how many tickets?: ")
    else:
        sold = int(sold)
        if sold <= limit and sold <= remaining_tickets:
             print(f'Alright, here are {sold} tickets!')
             return sold
        else:
            print('Sorry, we do not have enough tickets!')
    # return sold

buyer(20)