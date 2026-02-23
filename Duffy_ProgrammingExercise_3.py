# A program that calculates the user's total monthly expenses

import functools

def calculator(expenses):
    # Return safe empty results if the user entered no expenses.
    if len(expenses) == 0:
        return 0, None, None, [], []

    # Reduce the expense list into a single total by addin each record's amount.
    total = functools.reduce(lambda running_total, current_record: running_total + current_record[1], expenses, 0)

    # Reduce the expense list into the single record with the highest amount with first winning a tie.
    max_record = functools.reduce(lambda best_record, current_record:
            best_record if best_record[1] >= current_record[1] else current_record, expenses)

    # Reduce the expense list into the single record with the lowest amount with first winning a tie.
    min_record = functools.reduce(lambda best_record, current_record:
            best_record if best_record[1] <= current_record[1] else current_record, expenses)

    # Store the winning max and min amounts so we can collect tied records.
    max_amount = max_record[1]
    min_amount = min_record[1]

    # Collect all records that tie for the maximum or minimum amount in entry order.
    max_ties = [expense_record for expense_record in expenses if expense_record[1] == max_amount]
    min_ties = [expense_record for expense_record in expenses if expense_record[1] == min_amount]

    # Return the total, the winning max and min records, and the tie lists.
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