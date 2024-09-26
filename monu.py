class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

# Example usage
if __name__ == "__main__":
    # Create a new bank account
    account = BankAccount("123456", "Alice Smith")

    # Deposit some money
    account.deposit(500)

    # Check balance
    account.check_balance()

    # Withdraw some money
    account.withdraw(200)

    # Check balance again
    account.check_balance()

    # Try to withdraw more than the balance
    account.withdraw(400)

    # Final balance check
    account.check_balance()
