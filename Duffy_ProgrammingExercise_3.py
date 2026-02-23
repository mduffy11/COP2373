# A program that calculates the user's total monthly expenses.

import functools

def inquisitor():
    """
    Prompts the user to enter monthly expenses as name-and-amount records.

    Parameters:
        None

    Variables:
        expenses (list): Stores all entered records as [name, amount].
        record (list): Stores one expense record as [name, amount].
        record_name (str): The expense name entered by the user.
        record_amount (str): The raw amount input entered by the user before conversion.
        amount (float): The validated monthly amount rounded to two decimals.

    Logic:
        1. Initialize an empty list to store expense records.
        2. Loop until the user presses Enter on an expense name.
        3. Validate and convert the amount to a float rounded to two decimals.
        4. Reject invalid numbers and reject amounts less than $0.01.
        5. Append each completed record to the list.
        6. Return the list of expense records.

    Return:
        list: The list of expense records entered by the user.
    """
    # Initialize the list that stores all expense records.
    expenses = []

    # Repeat prompts until the user finishes by pressing Enter on the expense name.
    while True:
        # Reset the record list for each new expense entry.
        record = []

        # Read the expense name and finish input if it is blank.
        record_name = input("What is your expense? ").strip()
        if record_name == "":
            return expenses

        # Store the expense name in the record.
        record.append(record_name)

        # Repeat amount input until a valid monthly amount is entered.
        while True:
            record_amount = input("How much does that cost each month? ").strip()
            try:
                amount = round(float(record_amount), 2)
                if amount < 0.01:
                    print("Amount must be at least $0.01. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a valid dollar amount.")

        # Store the validated amount and save the record.
        record.append(amount)
        expenses.append(record)


def calculator(expenses):
    """
    Analyzes a list of monthly expense records and calculates summary statistics.

    Parameters:
        expenses (list): A list of expense records, where each record is [name (str), amount (float)].

    Variables:
        total (float): The sum of all monthly expense amounts.
        max_record (list): The single expense record with the highest amount (first wins ties).
        min_record (list): The single expense record with the lowest amount (first wins ties).
        max_amount (float): The highest amount used to detect ties.
        min_amount (float): The lowest amount used to detect ties.
        max_ties (list): All records tied for the highest amount in entry order.
        min_ties (list): All records tied for the lowest amount in entry order.

    Logic:
        1. Return safe empty results if the list of expenses is empty.
        2. Use functools.reduce to sum all amounts into a total.
        3. Use functools.reduce to select the record with the highest amount (first wins ties).
        4. Use functools.reduce to select the record with the lowest amount (first wins ties).
        5. Collect all records tied for the highest amount.
        6. Collect all records tied for the lowest amount.
        7. Return the calculated values.

    Return:
        tuple: (total, max_record, min_record, max_ties, min_ties)
    """
    # Return safe empty results if the user entered no expenses.
    if len(expenses) == 0:
        return 0, None, None, [], []

    # Sum all expense amounts into one monthly total.
    total = functools.reduce(lambda running_total, current_record:
        running_total + current_record[1], expenses, 0)

    # Select the record with the highest amount and keep the first record in a tie.
    max_record = functools.reduce(lambda best_record, current_record:
            best_record if best_record[1] >= current_record[1] else current_record, expenses)

    # Select the record with the lowest amount and keep the first record in a tie.
    min_record = functools.reduce(lambda best_record, current_record:
            best_record if best_record[1] <= current_record[1] else current_record, expenses)

    # Store winning amounts to detect ties across the full list.
    max_amount = max_record[1]
    min_amount = min_record[1]

    # Collect all records tied for maximum and minimum amounts in entry order.
    max_ties = [expense_record for expense_record in expenses if expense_record[1] == max_amount]
    min_ties = [expense_record for expense_record in expenses if expense_record[1] == min_amount]

    # Return all calculated values for printing in main().
    return total, max_record, min_record, max_ties, min_ties


def main():
    """
    Runs the monthly budget calculator by collecting input, analyzing expenses, and printing results.

    Parameters:
        None

    Variables:
        expenses (list): The list of expense records returned by inquisitor().
        total (float): The monthly total returned by calculator().
        max_record (list): The single highest expense record returned by calculator().
        min_record (list): The single lowest expense record returned by calculator().
        max_ties (list): The list of records tied for highest amount returned by calculator().
        min_ties (list): The list of records tied for lowest amount returned by calculator().
        record (list): A record used when printing tied results.

    Logic:
        1. Print program instructions.
        2. Collect expense records from the user.
        3. Handle the case where no expenses are entered.
        4. Call calculator() to compute totals and extremes using reduce.
        5. Print the total, highest, and lowest expenses with labels and currency formatting.
        6. Print tied records when more than one record shares the max or min amount.

    Return:
        None
    """
    # Print instructions and explain how to finish entering expenses.
    print("Welcome to the Monthly Budget Calculator.")
    print("This expense calculator will ask you to enter your expenses.")
    print("Enter the name of each expense, and then enter its monthly cost.")
    print("When you are finished, press Enter instead of entering another expense.\n")

    # Collect the user's expense records.
    expenses = inquisitor()

    # Handle the case where the user entered no expenses.
    if len(expenses) == 0:
        print("No expenses were entered, so there is nothing to calculate.")
        return

    # Calculate the total, min, max, and tie lists using reduce.
    total, max_record, min_record, max_ties, min_ties = calculator(expenses)

    # Print the total monthly expense as currency.
    print(f"\nTotal monthly expenses: ${total:.2f}")

    # Print the highest expense and list ties if more than one exists.
    if len(max_ties) > 1:
        print("Highest expenses (tied):")
        for record in max_ties:
            print(f"  {record[0]}: ${record[1]:.2f}")
    else:
        print(f"Highest expense: {max_record[0]}: ${max_record[1]:.2f}")

    # Print the lowest expense and list ties if more than one exists.
    if len(min_ties) > 1:
        print("Lowest expenses (tied):")
        for record in min_ties:
            print(f"  {record[0]}: ${record[1]:.2f}")
    else:
        print(f"Lowest expense: {min_record[0]}: ${min_record[1]:.2f}")


if __name__ == "__main__":
    main()