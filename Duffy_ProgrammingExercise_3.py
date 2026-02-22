# A program that calculates the user's total monthly expenses

# Import reduce function
import functools

# A function to process exense calculations
def calculator(expenses):
    # Calculate monthly expense total
    total = functools.reduce(lambda accumulator, current_record: accumulator + current_record[1], expenses, 0)
    # Initialize variables for the minimum and maximum
    max_record = None
    min_record = None
    max_ties = []
    min_ties = []
    # Return all calculated values
    return total, max_record, min_record, max_ties, min_ties

# A function to ask the user about their expenses
def inquisitor():
    # initialize variables for list of expenses
    expenses = []
    # intialize varaible for each record
    while True:
        # reset varaible for each record
        record = []  # reset for each new expense record
        # Ask the user for the name of their expenses
        record_name = input("What is your expense? ").strip()
        # End the program if they Press Enter
        if record_name == "":
            return expenses
        # Add the name to the record
        record.append(record_name)
        # Ask the user for the amount of that expense
        # ask for the amount (validate + convert + round)
        while True:
            record_amount = input("How much does that cost each month? ").strip()
            # Validate the data by trying to round to nearest cent
            try:
                amount = round(float(record_amount), 2)
                # Reject amounts less than 1 penny.
                if amount < 0.01:
                    print("Amount must be at least $0.01. Try again.")
                    continue
                break
            # Reject no numerical inputs.
            except ValueError:
                print("Please enter a valid dollar amount.")

        record.append(amount)
        # Add the record to the expense list
        expenses.append(record)



    # Explain how it works to the user
    print("This expense calculator will ask you to enter your expenses")
    print("when you are finished,just hit enter instead of entering another expense")