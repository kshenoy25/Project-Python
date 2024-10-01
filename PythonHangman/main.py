
# set of words
from wordslist import words
import random


# dictionary of key:()
hangman_art =  {             0: ("   ",
                                 "   ",
                                 "   "),
                             1: (" o ",
                                 "   ",
                                 "   "),
                             2: (" o ",
                                 " | ",
                                 "   "),
                             3: (" o ",
                                 "/| ",
                                 "   "),
                             4: (" o ",
                                 "/|\\",
                                 "   "),
                              5: (" o ",
                                  "/|\\",
                                  "/  "),
                              6: (" o ",
                                  "/|\\",
                                  "/ \\")}

# use double back-slash to print the slash

def display_man (wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    # for each character within hint, perform a join function
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    # list of underscore characters
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        #display_answer(answer)
        guess = input("Guess a letter: ").lower()

        # input validation breaking condition for a single character or an integer
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        # keeping track of the letters already guessed
        guessed_letters.add(guess)

        # guess equals a letter
        if guess in answer:
            # iterate loop once for each character in the answer
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # incrementing wrong guesses
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You winn!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lose!")
            is_running = False

    #print(hint)
    #print(answer)

if __name__ == "__main__":
    main()
