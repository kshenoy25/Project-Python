#### Choose Your Own Adventure!!! ####

name = input("Enter your name? ")
print("Welcome " + name + " to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input(" You have arrived at a dark forrest...you walk through the forrest or run around it. But it maybe not safe. Type run or walk as your action.")

    if answer == "run":
        print("You chose to run around the forrest. You may reach the end of the forrest quickly BUT a werewolf has found your scent and will rip you apart.")
    elif answer == "walk":
        print("You chose to walk through the forrest. You are not alone in the forrest for there is a huge spider famished for human flesh. You have been taken.")
    else:
        print("Not a valid option. You lose.")

elif answer =="right":
    answer = input("You have come to a bridge. It looks pretty wobbly. Do you want to cross it or head back (cross/back)")

    if answer == "back":
        print("You chose to head back. Too bad there's a man with a chainsaw ready to slash you....")
    if answer == "cross":
        answer = input("You crossed the bridge and there's a stranger. Do you talk to them? (y/n)")

        if answer == "y":
            print("You talked to the stranger. Very interesting because now the stranger has a gift for you. 3 gold bars and a safe passage to the village. Hurray!")
        elif answer == "n":
            print("You ignore the stranger. The stranger does not like that and takes a sword and slices your legs off. You lose.")
        else:
            print("Not a valid option. You lose.")
else:
    print("Not a valid option")

print("Thanks for playing!", name)