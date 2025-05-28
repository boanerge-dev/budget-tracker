# Simple Python Budget Tracker

def show_menu():
    print("\n--- Budget Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

def main():
    balance = 0.0

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            income = float(input("Enter income amount: "))
            balance += income
            print(f"Income added. New balance: ${balance:.2f}")

        elif choice == '2':
            expense = float(input("Enter expense amount: "))
            if expense > balance:
                print("Insufficient balance!")
            else:
                balance -= expense
                print(f"Expense added. New balance: ${balance:.2f}")

        elif choice == '3':
            print(f"Current balance: ${balance:.2f}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
