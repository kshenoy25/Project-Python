from itertools import count


def show_balance(balance):
    print("************************")
    print(f"Your balance is ${balance:.2f}")
    print("************************")


def deposit():
    print("************************")
    # using float for dollars and cents
    amount = float(input("How much would you like to deposit? "))
    print("************************")

    if amount < 0:
        print("************************")
        print("Sorry, you can't deposit negative amount")
        print("************************")

        return 0
    else:
        return amount


def withdraw(balance):
    print("************************")
    amount = float(input("How much would you like to withdraw? "))
    print("************************")

    if amount > balance:
        print("************************")
        print("Sorry, insufficient funds")
        print("************************")

        return 0
    elif amount < 0:
        print("************************")
        print("Sorry, amount must be greater than 0")
        print("************************")

        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("    Shenoy Banking    ")
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("************************")


        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            # add deposit to balance
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("************************")
            print("Invalid choice")

    print("Thank you for using Banking Shenoy!")


if __name__ == '__main__':
    main()