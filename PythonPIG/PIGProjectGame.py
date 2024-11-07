# generate a random number
import random


def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll
#print(value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid. Try again.")

max_score = 50
player_scores = [0 for _ in range(players)] # list contains all individual scores

# go through player terms

while max(player_scores) < max_score:
    for player_idx in range(players): # looping through players so they each get a turn
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        print("Your total score is: " , player_scores[player_idx], "\n")
        current_score = 0 # for the turn
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:" , value)
            print("Your score is: ", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])

max_score = max(player_scores)
player_winning_idx = player_scores.index(max_score)
print("Player number", player_winning_idx + 1, "is the winner with a score of" , max_score)