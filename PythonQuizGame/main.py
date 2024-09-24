# new quiz game function
def new_game():
    guesses = []
    correct_guesses = 0

    # represents the first question
    question_number = 1

    for key in questions:
        print("-----------")
        print(key)
        # effectively receive 0 as the index
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)


        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1
    display_score(correct_guesses, guesses)

    # pass
# ---------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("INCORRECT!")
        return 0

    # pass
# ---------------------
def display_score(correct_guesses, guesses):
    print("-----------")
    print("RESULTS")
    print("-----------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int ((correct_guesses/ len(questions)) * 100)
    print("Your score is " + str(score) + "%")

    # pass
# ---------------------
def play_again():
    response = input("Would you like to play again? (Y/N): ")
    response = response.upper()
    if response == "Y":
        return True
    else:
        return False

    #pass
# ---------------------

# note: dictionaries are comprised of key value pairs
questions = {

    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"

}
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. Who's Earth?"]]

new_game()

while play_again():
    new_game()
print("Good-Bye")