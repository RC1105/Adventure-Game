'''
This module had functions for the user choices
'''
from time import *
import Global

def clear():
    from os import system,name
    if name=='nt':
        return system('cls')

def arsenal():
    print('1. Flame Thrower\n2. Handgun\n3. Shark Jab\n4. Fish net')
    selected=(input("Which weapons do you pick for this underwater investigation? : "))
    for i in selected.split():
        if i=='1':
            Global.inventory.append('Flame Thrower')
        elif i=='2':
            Global.inventory.append('Handgun')
        elif i=='3':
            Global.inventory.append('Shark Jab')
        elif i=='4':
            Global.inventory.append('Fish net')

def start():
    text="As you put on your diving gear, a motor boat takes you to the dive point. The scortching sun and warm breeze tingle your senses.\nThis could be dangerous."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print()
    Global.rest(2) # clear text after 3 sec
    print()
    print('1. Dive in\n2. Abort the mission')
    selected=int(input("What do you do? : "))
    print()
    if selected==1:
        Global.score +=10
        return 1
    elif selected ==2:
        return 0
    else:
       wrong_input()

def sea_snake():
    text="Within a few a minutes, you and your team are deep beneath the water surface. It's getting darker and quieter.\nNot sooner, you feel something slither by your left foot. It's what appears to be a sea snake!"
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Hide behind corals\n2. Use a weapon\n3. Quietly swim ahead")
    selected=int(input("What do you do? : "))
    print()
    
    if selected==1:
        text="You hide behind nearby corals and wait for the sea snake to pass by.\nOuch! Something pinches your hand. It's a crab and your foot is bleeding."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        Global.rest(2)
        print('Press 1 for taking first aid. Else press any other key')
        #print('1. Surface back for first aid\n2. Continue your mission')
        choice=(input("What do you do? : "))
        if choice!='1':
            Global.health -= 1
        Global.score +=5
        return 1
    elif selected == 2:
        for i in range(len(Global.inventory)):
            print(i+1,Global.inventory[i])
        weapon=int(input("Which weapon do you choose? :"))
        print()
        text="Just as you are about to attack with your weapon, the venomous sea snake curls around you foot and bites into your flesh. the venom runs through your viens and you begin to loose conciousness."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        Global.rest(2)
        return 0
    elif selected == 3:
        Global.score +=10
        return 1
    else:
        wrong_input()

def shark():
    text="Good move! The sea snake passes and you are safe. As you swim deeper into the waters, you encounter a hammerhead shark.\nThe shark is approaching you."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    if Global.health==0:
        text="The hammerhead sharks are known for their incredible sense of smell.\nThe shark picks up the scent of your blood and comes staright for you within no time."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        return 0
    else:
        print("1. Attack its fin\n2. Attack its nose\n3. Qiuetly swim ahead")
        select=int(input("What do you do? : "))
        print('\n')
        if select==1:
            text="You just proved the shark. It attacks back and bites into your flesh with great force."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print()
            return 0
        elif select==2:
            Global.score +=10
            return 1
        elif select==3:
            text="You try to quietly escape the scene, but the shark detects your motion in the water. It attacks you and your team."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print()
            return 0
        else:
            wrong_input()


def ocean_current():
    text="As the deadly shark approaches, you jab the shark on it nose - its weak spot, with all your effort.\nAfter a few hits, the shark is heavily injured and swims away in defence. You lead your team deeper towards the detected submarine.\nSuddenly, you find yourself caught in an ocean current. It is cold and strong. The current is dragging you along with it mercilessly."
    for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Swim parallel to the current\n2. Swim against the current\n3. Swim diagonal to the current")
    select=int(input("What do you do? : "))
    if select == 1:
        text="You curl your body inwards and allow the current to carry your body along. You reach an unknown dark space and are separated from your team.\nYou are lost underwater."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        return 0
    elif select == 2:
        text="The current is too strong to swim against and it carries you along with it to an unknown dark space. You are alone and lost."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        return 0
    elif select == 3:
        Global.score +=10
        return 1
    else:
        wrong_input()

def team_mate():
    text="Phew! That was close. You successfully get yourself out of the strong current.\nContinuing the mission, you guide yout team towards the submarine that is now faintly visible from the torch light your team mates turned on.\n\nTeam mate: Commander, do you think this is a trap? The submarine is in plain sight!"
    for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Look for traps\n2. Explore inside the submarine")
    select=int(input("What do you do? : "))
    if select == 1:
        Global.score +=10
        return 1
    elif select == 2:
        text="A biometric sensor detects unauthorised personnel and foes into self destruct mode."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        return 0
    else:
        wrong_input()
    
def sensor():
    text="Looks like your team was right. You find a biometric sensor lock and its control switch at the back of the submarine."
    for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print('1. Manually disable\n2. Break the ciruitry')
    select=int(input("How will you disable this lock? : "))
    if select == 1:
        Global.score +=10
        return 1
    elif select == 2:
        text="Your attempt fails. The submarine enters self destruct mode."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        return 0
    else:
        wrong_input()

def keypad():
    text="The biometric locks are disable. You also see a lockout trunk open. The ship must have been abandoned by its crew in some sort of distress.\nWhat could have happened? You enter the submarine through the chamber.\nInside the submarine, you see a poorly maintained ship. It appears as though the ship was abandoned for a very long time now. But why was it only recently detected? Many questions arise.\nYour thoughts are interupted when a beep sound is heard.\n\nIn front of you is a sealed vault with a keypad lock."
    for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Break into the vault\n2. Look for clues to the lock")
    select=int(input("What do you do? : "))
    if select==1:
        text="Your attempt fails. The submarine enters self destruct mode."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print()
        return 0
    elif select==2:
        Global.score +=10
        return 1
    else:
        wrong_input()

def tap():
    text="As you explore around the ship, you happened to hear a repeated tapping sound."
    for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Investigate the sound\n2. Continue exploring")
    select=int(input("What do you do? : "))
    print('\n')
    if select == 1:
        text="You follow the tapping sound and it leads you to the control room. There is a stop watch lying on the control panel and it appears to be the source of sound. Making your way through the room, you grab the stop watch and open it.\nIt was a trap. THe doors of the control room are shutting down"
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        print("1. Run for the door and explore further\n2. Try to stop the doors from closing")
        choice=int(input("What do you do? : "))
        print('\n')
        if choice==1:
            return tap()
        elif choice==2:
            text="Your attempt fails. You and your team is locked in the control room with no way of escape."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print('\n')
            return 0
        else:
            wrong_input()
    elif select ==2:
        Global.score +=10
        return 1
    else:
        wrong_input()

def journal():
    text="You dismiss the tapping sound and continue walking across the hallway. The lights are getting dimmer and the sound of engines is rising. You are heading towards the engine room.\n\nUpon arrival you find a journal and flip across a few pages, until a particular page grabs your attention.\nThe entry of the journal is dated 01-Aug-2012. Below you see a schematic sketch of a nuclear bomb. It is followed by some text:\n\nWe will get justice. We deserve it. Victory shall be ours within the next 24 hours. I'm leaving this ship to save my crew from the horrors that are yet to come. We will get what is ours.\n\nCould this mean that the vault holds a nuclear bomb?!"
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Abort the mission and escape\n2. Keep looking for clues")
    select=int(input("What do you do? : "))
    if select==1:
        text="You immediatly call for you team and begin an escape procedure. As your first team mate leaves the submarine through the escape chamber, an internal sensor sets the ship into self destruct mode. It's too late."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        return 0
    elif select == 2:
        Global.score +=10
        return 1
    else:
        wrong_input()
        
def split():
    text="If what the journal says is right, you are to lead a team to find a nuclear bomb on this ship and diffuse it withing 24 hours.\nWould splitting the team be an ideal descision?"
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Split the team\n2. Stick together")
    choice_1=int(input("What do you do? : "))
    print('\n')
    if choice_1==1:
        Global.score +=10
        text="The team splits its ways to find clues to unlock the vault. Suddenly, you hear a thud sound.\nOne of your team mates has been locked in a cell. Turns out it was wise to split the team.\n\nAs you walk along a corridor in search for clues, you encounter a steep turn. It's dark and has a pungent odour.\nYou walk in deeper to realise this is not an ordinary submarine - It's a prison. Ahead of you are atleast a hundred cells each holding a prisoner that has been tied upto their mouths in order to muffle their voices.\n\nMaybe they are being held hostages. Something is not right, and you must find out fast. As you come closer to a cell, you notice that all people are pointing three fingers up.\nWhat could this mean?"
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        print("1. Go to cell 3\n2. Type '3' in the keyboard")
        choice_2=int(input("What do you do? : "))
        if choice_2==1:
            Global.score +=10
            return 1
        elif choice_2==2:
            text="You quickly run for the keypad of the vault and type in '3'.\nThat's the incorrect password."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print('\n')
            return 0
    elif choice==2:
        text="As you move further, a capture cage falls on your entire team. You are trapped."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        return 0
    else:
        wrong_input()

def cell3():
    text="You walk towards cell 3. It is empty! Looks like the hostage has tried to escape..."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Look for the hostage\n2. Investigate the empty cell")
    select=int(input("What do you do? : "))
    if select==1:
        text="Looking for the hostage, you walk further along the dark corrider.\nTHUD! A prison cage falls upon you and you are trapped. You have no means of contact and your team is now without a commander."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        return 0
    elif select==2:
        Global.score +=10
        return 1
    else:
        wrong_input()

def chooseInput():
    text="While investigating around the cell, you find three mysterious boxes.\nYou can select any two boxes and open simultaneously."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Box 1\n2. Box 2\n3. Box 3")
    c_4,c_5=input("Which two boxes do you choose? : ").split()
    print('\n')
    c_4=int(c_4)
    c_5=int(c_5)
    if (c_4==1 and c_5==2) or (c_4==2 and c_5==1):
        text="Box 1 has a clue! It says H2O-->Box 2\nBox 2 seems to be epmty."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        Global.rest(2)
        print('1. Pour water from the ocean into box 2\n2. Check out the other boxes')
        select=int(input("What do you do? : "))
        print('\n')
        if select==1:
            Global.score +=10
            return 1
        elif select==2:
            return (chooseInput())
    elif (c_4==2 and c_5==3) or (c_4==3 and c_5==2):
        text='Box 2 seems to be empty.\nBox 3 has a note. The note says, "The bomb will now be active in 12 hours."\n\nOh no! Looks like the third box just reduced our time to diffuse the nuclear bomb.'
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        Global.rest(2)
        print("1. Type '12' in keypad2\n2. Check out the other boxes")
        select=int(input("What do you do? : "))
        if select==1:
            text="Unfortunately, that's the wrong password."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
             #print('\n')
            Global.rest(2)
            return 0
        elif select==2:
            return(chooseInput())
    elif (c_4==3 and c_5==1) or (c_4==1 and c_5==3):
        text="Box 1 has a clue! It says H2O-->Box 2\nBox 3 has a note. The note says, 'The bomb will now be active in 12 hours.'\n\nOh no! Looks like the third box just reduced our time to diffuse the nuclear bomb."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        Global.rest(2)
        print("1. Pour water from ocean into box 2\n2. Check out the other boxes")
        select=int(input("What do you do? : "))
        print('\n')
        if select==1:
            Global.score +=10
            return 1
        elif select==2:
            return (chooseInput())
    else:
        wrong_input()

    
def box2():
    text="You head towards the lockout trunk to fill the Box 2 with water, as instructed by the clue from Box 1.\nWoah! As you fill water in the Box, writings on the bottom begin to appear --> dd-mm-yyyy\nThis format resembles the keypad outside the vault."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print('\n')
    Global.rest(2)
    print("1. Type in keypad current date\n2. Type in keypad your date of birth\n3. Type in keyboard the date of journal entry")
    select=int(input("What do you do? : "))
    if select==1 or select ==2:
        text="Unfortunately that's the wrong password."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        return 0
    elif select==3:
        print('\n')
        text="Well played! You have entered the vault. You can see the nuclear bomb, eclosed in a glass case.\nThere is an inscription on the glass: 'As the water rises, the Earth rolls out and all will be saved.'\n\nIn front of the glass casing, you can see 5 deep cuts in the floor. Each cut has an small object placed within - Cube, Diamond, Pyramid, Sphere and Cylinder."
        for i in text: #loop to print text letter by letter
            print(i,end="",flush=True)
            Global.rest(0.1)
        print('\n')
        Global.rest(2)
        print("1. Try pouring water from Box 2 into these cuts\n2. Smash the glass casing with box 2 and try to diffuse the nuclear bomb")
        choice=int(input("What do you do? : "))
        if choice==1:
            Global.score +=10
            return 1
        elif choice==2:
            text="You hop over the deep cuts and smash the entire glass casing with the box 2, which trigers the bomb.\nIt explodes."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print('\n')
            return 0
        else:
            wrong_input()

def chooseShape():
    chances=3
    while chances>0:
        print("1. Diamond\n2. Cube\n3. Cylinder\n4. Sphere\n5. Pyramid")
        select=int(input("In which shape you do pour the water? : "))
        if select==4:
            text="As you pour the sea water from the box 2, the sphere rises up until it rolls over the floor beside you.\nYou were right. This must have been the representation of the Earth, as mentioned on the inscription on the glass.\nThe timer on the bomb has stopped and you have successfully deactivated the nuclear bomb."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print('\n')
            Global.score +=10
            return 1
        elif select in (2,3,4,5):
            text="As you pour the sea water from the box 2, the sphere rises up until it rolls over the floor beside you.\nNothing happens."
            for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
            print('\n')
            chance-=1
        text="The water in the box is over and the vault behind you has been locked. You are stuck inside."
        for i in text: #loop to print text letter by letter
                print(i,end="",flush=True)
                Global.rest(0.1)
        print('\n')
        return 0
    else:
        wrong_input()
        
def win():
    print("Congratulations on succeeding this mission.")
    print("You have scored",Global.score,"points!") #Displaying points

def loss():
    print("Commander",Global.name,",this is the end your mission. Game over")
    print("You have scored",Global.score,"points!") #Displaying points

def wrong_input():
    print("\nINCORRECT INPUT")
