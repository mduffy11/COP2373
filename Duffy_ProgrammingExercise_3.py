# A program that calculates the user's total monthly expenses.

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