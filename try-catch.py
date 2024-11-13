class InsufficientFundsError(Exception):
    """Custom exception raised when attempting to withdraw more than available balance."""

    def __init__(self, message="Insufficient funds in your account."):
        self.message = message
        super().__init__(self.message)


class NegativeAmountError(Exception):
    """Custom exception raised when a negative amount is entered for a transaction."""

    def __init__(self, message="Amount must be positive."):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise NegativeAmountError("Cannot deposit a negative or zero amount.")
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        except NegativeAmountError as e:
            print(f"Deposit failed: {e}")
            raise  # Re-raise exception for higher-level handling if needed

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise NegativeAmountError("Cannot withdraw a negative or zero amount.")
            if amount > self.balance:
                raise InsufficientFundsError("Attempted to withdraw more than available balance.")
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        except (NegativeAmountError, InsufficientFundsError) as e:
            print(f"Withdrawal failed: {e}")
            raise  # Re-raise for further handling if needed

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")
        return self.balance


def perform_transactions(account):
    """Function to demonstrate exception handling with try, except, and raise."""
    try:
        print("\nStarting transactions...")

        # Attempt deposit with positive and negative values
        try:
            account.deposit(500)
            account.deposit(-100)  # This should trigger NegativeAmountError
        except NegativeAmountError as e:
            print(f"Handled a deposit error: {e}")

        # Attempt withdrawal with valid and invalid amounts
        try:
            account.withdraw(200)
            account.withdraw(1000)  # This should trigger InsufficientFundsError
        except InsufficientFundsError as e:
            print(f"Handled a withdrawal error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise  # Re-raise to ensure unexpected errors aren't silently swallowed
    finally:
        print("Transaction session ended.\n")
        

# Main execution
if __name__ == "__main__":
    try:
        # Create a bank account with a starting balance
        my_account = BankAccount("Alice", balance=1000)

        # Perform various transactions and handle exceptions as they occur
        perform_transactions(my_account)

        # Check final balance
        my_account.check_balance()

    except Exception as e:
        # Handle any unexpected exceptions that weren't already handled
        print(f"Critical error: {e}")
    finally:
        print("End of banking operations. Thank you for using our service.")
