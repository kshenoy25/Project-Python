import random

# dictionary = made up of key value pairs where the value is a tuple

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

# ● ┌ ─ ┐ │ └ ┘
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# list of dice randomly generated from 1 through 6

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

# generate a random number

for die in range(num_of_dice):
   dice.append(random.randint(1,6))

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# the nested for loop below showcases how to print the die in a horizontal fashion
for line in range(5):
    for die in dice:
        # die is the number 1 - 6
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    # += the current value
    total += die
print(f"total: {total}")
