import turtle

WIDTH, HEIGHT = 500, 500

# create the turtle screen
screen = turtle.Screen()
screen.title("The Turtle Race")
screen.setup(WIDTH, HEIGHT)



def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers) # checking if it numeric
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range 2-10. Try again!")


racers = get_number_of_racers()
print(racers)