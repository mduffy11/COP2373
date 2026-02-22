# A program that calculates the user's total monthly expenses.

# A function to ask the user about their expenses
def inquisitor():
    # initialize variables for list of expenses and each record
    expenses = []
    record = []
    # Explain how it works to the user
    print("This expense calculator will ask you to enter your expenses")
    print("when you are finished,just hit enter instead of entering another expense")
    # Ask the user for the name of their expenses
    record[0] = input("What is your expense? ")
    record[1] = input("How much does that cost each month? ")
    # Add that item to the list
    expenses.append(record)