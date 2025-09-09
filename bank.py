# Banking System Simulation

# Store user data: key = account number, value = dict with 'name' and 'balance'
bank_data = {}
account_counter = 1001  # Starting account number


def create_account(name):
    global account_counter
    account_number = account_counter
    bank_data[account_number] = {"name": name, "balance": 0.0}
    account_counter += 1
    print(f"Account created successfully! Account Number: {account_number}")


def deposit(account_number, amount):
    if account_number in bank_data:
        bank_data[account_number]["balance"] += amount
        print(f"Deposited ₹{amount:.2f}. New Balance: ₹{bank_data[account_number]['balance']:.2f}")
    else:
        print("Invalid account number.")


def withdraw(account_number, amount):
    if account_number in bank_data:
        if bank_data[account_number]["balance"] >= amount:
            bank_data[account_number]["balance"] -= amount
            print(f"Withdrawn ₹{amount:.2f}. New Balance: ₹{bank_data[account_number]['balance']:.2f}")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid account number.")


def check_balance(account_number):
    if account_number in bank_data:
        print(f"Account Holder: {bank_data[account_number]['name']}")
        print(f"Current Balance: ₹{bank_data[account_number]['balance']:.2f}")
    else:
        print("Invalid account number.")


def main():
    print("=== Welcome to Python Bank ===")
    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter your name: ")
            create_account(name)

        elif choice == '2':
            try:
                acc = int(input("Enter account number: "))
                amt = float(input("Enter amount to deposit: "))
                deposit(acc, amt)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            try:
                acc = int(input("Enter account number: "))
                amt = float(input("Enter amount to withdraw: "))
                withdraw(acc, amt)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            try:
                acc = int(input("Enter account number: "))
                check_balance(acc)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Thank you for using Python Bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()