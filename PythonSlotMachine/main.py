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

def get_pay_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐️':
            return bet * 20
    return 0



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

        payout = get_pay_out(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print(f"You lost this round")
        balance += payout

        play_again = input("Would you like to play again? (y/n) ").upper()
        if play_again != "Y":
            break

    print("**********************************")
    print(f"Game over. Final balance is {balance}!")
    print("**********************************")
if __name__ == '__main__':
    main()