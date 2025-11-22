#ATM simulator

def check_balance(balance, history):
    print(f"Your balance is ${balance:.2f}")
    history.append(f"Checked balance: {balance:.2f}")

def deposit(balance, deposit_amount, history):
    balance += deposit_amount
    print(f"${deposit_amount:.2f} deposited successfully")
    history.append(f"Deposited ${deposit_amount:.2f} | New balance: ${balance:.2f}")
    return balance

def withdraw(balance, withdraw_amount, history):
    if withdraw_amount > balance:
       print(f"Insufficient funds to withdraw ${withdraw_amount:.2f}")
       history.append(f"Failed withdrawal attempt: ${withdraw_amount:.2f} | Balance: ${balance:.2f}")
    else:
        balance -= withdraw_amount
        print(f"${withdraw_amount:.2f} withdrawn successfully and your present account balance is ${balance:.2f}")
        history.append(f"Withdrew ${withdraw_amount:.2f} | New balance: ${balance:.2f}")
    return balance

def show_history(history):
    print("\n--- Transaction History ---")
    if not history:
        print("No transactions yet.")
    else:
        for record in history:
            print(record)

def atm_simulator():
    balance = 1000
    history = []
    while True:
        print("\n--- Welcome to the ATM simulator ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Show Transaction History")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_balance(balance, history)
        elif choice == 2:
            amount = float(input("Enter the amount you want to deposit:$ "))
            balance = deposit(balance, amount, history)
        elif choice == 3:
            amount = float(input("Enter the amount you want to withdraw:$ "))
            balance = withdraw(balance, amount, history)
        elif choice == 4:
            show_history(history)
        elif choice == 5:
            print("Thank you for using the ATM simulator")
            break
        else:
            print("Invalid choice. Please try again.")

atm_simulator()
