import random
while True:

    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your choice: ").lower()
        # win conditions
    if player == computer_choice:
        print("Computer's choice: ", computer_choice)
        print("Player choice: ", player)
        print("Tie")

    elif player == "rock":
        if computer_choice == "paper":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Lose!")
        if computer_choice == "scissors":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Win!")

    elif player == "scissors":
        if computer_choice == "rock":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Lose!")
        if computer_choice == "paper":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Win!")

    elif player == "paper":
        if computer_choice == "scissors":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Lose!")
        if computer_choice == "rock":
            print("Computer's choice: ", computer_choice)
            print("Player choice: ", player)
            print("You Win!")

    play_again = input("Would you like to play again (Y/N)? ").lower()

    if play_again != "yes":
        break
print("Thank you for playing!")