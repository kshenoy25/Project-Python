import turtle
import time
import random

WIDTH, HEIGHT = 700, 600

COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]



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


def race(colors):
    turtles = create_turtles(colors) # create all turtles and know what colors the turtles are

    while True: # moving turtles one by one until the turtles reach the finish line

        for racer in turtles:
            distance = random.randrange(1,20) # moving turtle between 1 and 20 pixels
            racer.forward(distance)

            x, y = racer.pos() # gives position of the turtle
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)] # find the winning turtle color


def create_turtles(colors):
    turtles = [] # empty list because of unknown quantity of turtles

    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color) # color will come from the string that was created
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH// 2 + (i + 1) *  spacing_x, -HEIGHT// 2 + 20) # setting the initial position
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.title("The Turtle Race")
    screen.setup(WIDTH, HEIGHT)


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS) # take the list and randomize the items within
colors = COLORS[:racers]

winner = race(colors)
print("THE WINNER OF THE TURTLE RACE IS", winner)
time.sleep(5)

"""
# create a new turtle objects
racer = turtle.Turtle()
racer.speed(1)
racer.penup()
racer.shape("turtle")
racer.color("blue")
# gives degrees for the turns
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.right(90)
racer.backward(100)

racer2 = turtle.Turtle()
racer2.speed(5)
racer2.penup()
racer2.shape("turtle")
racer2.color("yellow")
# gives degrees for the turns
racer2.forward(100)
racer2.left(90)
racer2.pendown()
racer2.forward(150)
racer2.right(90)
racer2.backward(150)
# pause program for 5 seconds to see where the turtle went before the window closes
#time.sleep(20)

"""
