# Define the BankAcct class.
class BankAcct:

    # Initialize the account state information.
    def __init__(self, name, account_number, balance, interest_rate):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        self.last_interest = 0.0

    # Deposit money into the account.
    def deposit(self, amount):
        # Reject deposits that are not greater than 0.
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        # Add the deposit amount to the balance.
        self.balance += amount

        # Display the deposit transaction.
        print(f"Deposited ${amount:.2f} into {self.name}.")

    # Withdraw money from the account.
    def withdraw(self, amount):
        # Reject withdrawals that are not greater than 0.
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        # Reject withdrawals that exceed the balance.
        if amount > self.balance:
            print("Insufficient funds.")
            return

        # Subtract the withdrawal amount from the balance.
        self.balance -= amount

        # Display the withdrawal transaction.
        print(f"Withdrew ${amount:.2f} from {self.name}.")

    # Set a new interest rate for the account.
    def set_interest_rate(self, new_rate):
        # Reject negative interest rates.
        if new_rate < 0:
            print("Interest rate cannot be negative.")
            return

        # Update the interest rate.
        self.interest_rate = new_rate

        # Display the updated interest rate.
        print(f"Interest rate for {self.name} set to {self.interest_rate:.4f}.")

    # Return the current account balance.
    def get_balance(self):
        return self.balance

    # Calculate and apply interest based on the number of days.
    def apply_interest(self, days):
        # Reject day values that are not greater than 0.
        if days <= 0:
            print("Number of days must be greater than 0.")
            return 0.0

        # Calculate the simple interest for the given number of days.
        interest = self.balance * self.interest_rate * (days / 365)

        # Store the last interest amount.
        self.last_interest = interest

        # Add the interest to the balance.
        self.balance += interest

        # Display the interest transaction.
        print(f"Applied ${interest:.2f} interest to {self.name} for {days} days.")

        # Return the interest amount.
        return interest

    # Return the formatted account information.
    def __str__(self):
        return (
            f"Account Name: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}\n"
            f"Interest Rate: {self.interest_rate:.4f}\n"
            f"Last Interest Earned: ${self.last_interest:.2f}\n"
        )


# Test the checking account methods.
def test_checking():
    # Create a checking account object.
    checking = BankAcct("Duffy Checking", "CHK-1001", 1200.00, 0.0010)

    # Display the starting account information.
    print("CHECKING ACCOUNT START")
    print(checking)

    # Deposit money into the checking account.
    checking.deposit(300.00)

    # Withdraw money from the checking account.
    checking.withdraw(150.00)

    # Attempt to withdraw too much money from the checking account.
    checking.withdraw(2000.00)

    # Apply interest to the checking account.
    checking.apply_interest(30)

    # Display the current checking balance.
    print(f"Current checking balance: ${checking.get_balance():.2f}")
    print()

    # Display the ending account information.
    print("CHECKING ACCOUNT END")
    print(checking)


# Test the savings account methods.
def test_savings():
    # Create a savings account object.
    savings = BankAcct("Duffy Savings", "SAV-2001", 5000.00, 0.0350)

    # Display the starting account information.
    print("SAVINGS ACCOUNT START")
    print(savings)

    # Change the interest rate for the savings account.
    savings.set_interest_rate(0.0400)

    # Apply interest to the savings account.
    savings.apply_interest(60)

    # Display the current savings balance.
    print(f"Current savings balance: ${savings.get_balance():.2f}")
    print()

    # Display the ending account information.
    print("SAVINGS ACCOUNT END")
    print(savings)


# Run the selected account test.
def test(choice):
    # Run the checking account test if option 1 is selected.
    if choice == "1":
        test_checking()

    # Run the savings account test if option 2 is selected.
    elif choice == "2":
        test_savings()

    # Display an error message for an invalid selection.
    else:
        print("Invalid selection. Please run the program again and choose 1 or 2.")


# Start the program and collect the user's test choice.
def main():
    # Display the menu choices.
    print("Select an account test to run:")
    print("1. Checking Account")
    print("2. Savings Account")

    # Collect the user's choice.
    choice = input("Enter 1 or 2: ")

    # Run the chosen test.
    test(choice)


# Call the main function.
main()