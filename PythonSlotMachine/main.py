import random


def spin_row():
    symbols = [ "🍒", "🍉", "🍋", "🔔", "⭐️"]

    # list comprehension is an easy-to-read compact, and elegant way of creating a list from any existing iterable object
    # much more readable and efficient
    return [random.choice(symbols) for _ in range(3)]

#    results = []
#    for symbol in range(3):
#        results.append(random.choice(symbols))
#    return results

def print_row(row):
    # row = list
    # take iterable and join each element by space
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_pay_out():
    pass


def main():
    balance = 100
    print("************************")
    print("Welcome to Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("************************")

    while balance > 0:
        print(f"Current balance is {balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid bet amount")
            # will skip the current iteration of the loop and start from the beginning
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet


        row = spin_row()
        print("Spinning...\n")
        print_row(row)

if __name__ == '__main__':
    main()