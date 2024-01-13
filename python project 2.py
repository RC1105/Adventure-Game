choice_1 = input('Do you want to split your team into two groups/teams. Choose yes or no   \n')
choice_1=choice_1.lower()
print()


def chooseShape(count):
    print("1. Diamond \n2. Cube \n3. Cylinder\n4. Sphere\n5. Pyramid")
    a = int(input())
    if count == 0:
        print("You lost the game\n")
        exit()
    if a == 4:
        print("Congratulations! You won the game\n")
        exit()
    else:
        print("Only ", count, " chance/chances left")
        chooseShape(count - 1)


def checkInputs(time_in_sec):
    choice_4, choice_5 = chooseInput()
    choice_4 = int(choice_4)
    choice_5 = int(choice_5)
    if (time_in_sec == 0):
        print("Bomb has blasted. Time is Over. Good luck next time")
        exit()
    if (choice_4 == 1 and choice_5 == 2):
        print("Box 1 is H2O")
        DOBdata = input("please enter the DOB in dd-mm-yyyy\n")
        print(DOBdata)
        d, m, y = DOBdata.split("-")
        str1 = d + m + y

        print("Excellent choice. You are done with 80% of your game. Good luck for the remaining 20% of the game")
        input()
        return int(str1)


    elif (choice_4 == 1 and choice_5 == 3):
        print("Timer becomes half")
        print("Box 1 is H2O")
        time_in_sec = int(time_in_sec / 2)
        if (time_in_sec == 0):
            print("Bomb has blasted. Time is Over. Good luck next time")
            exit()
        temp = checkInputs(time_in_sec)

    elif (choice_4 == 2 and choice_5 == 3):

        DOBdata2 = input("please enter the DOB in dd-mm-yyyy\n")
        print(DOBdata2)
        print("Timer becomes half")
        time_in_sec = int(time_in_sec / 2)
        if (time_in_sec == 0):
            print("Bomb has blasted. Time is Over. Good luck next time")
            exit()
        temp = checkInputs(time_in_sec)


def chooseInput():
    c_4, c_5 = input(
        "While investigating you will find three boxes. you can choose and open any of the two boxes at a time. But not all three. choose the two box numbers at a time    1. Box one\n  2. Box two\n  3. Box three\n").split()
    return c_4, c_5


if (choice_1 == "yes"):
    print(
        "Good Choice, Now you had entered into the prison section. The people inside the prison are tied up their mouth with cloth, so that they can't talk but you are able to see the three fingers shown by the prisoners")
    print("So You have two choices now. Select the choice number\n")
    choice_2 = int(input("1.Go to Cell 3\n2.Type '3' in the keyboard\n"))
    if (choice_2 == 1):
        choice_3 = input(
            "Good move now you are into the pilot cell. Do you want to further investigate? choose yes or no\n")
        choice_3=choice_3.lower()
        if (choice_3 == "yes"):
            time_in_sec = 300
            dob = checkInputs(300)
            print(
                "Now you are in front of a big wall and there is a small keypad on the wall. Now you have to type the password containing 8 digits so that the wall gets open and you can go inside the room.\n")
            passwd = int(input())
            if (passwd != dob):
                print("You entered wrong password. Game over\n")
                exit()
            print(
                "Now you are inside the room. There are 5 different shapes inside glass tubes. Select the correct one to win the game using clues you found out in the three boxes.")
            chooseShape(2)
        elif (choice_3 == "no"):
            print("Game over. Good luck next time\n")
            exit()

    elif (choice_2 == 3):
        print("The game ends. Good luck next time")
        exit()

elif (choice_1 == "no"):
    print("Game has ended. Good luck next time")
    exit()
else:
    pass

