from time import *
import Functions
import Global


def Underwater():
    '''
    Intro
    '''
    Global.initialise_inventory()

    text="You are the commanding officer of an underwater exploration team.\nYou have been appointed to lead your team into the deep Indian Ocean to investigate \
    a foreign submarine that has been discovered two days ago."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print()
    Global.rest(3) # clear text after 3 sec
    Functions.clear()

    text="Captain: Ah! Commander, I was hoping to meet you. \nI'm sure you have been briefed about this mission.\nI wish you all the very best."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print()
    Global.rest(3) # clear text after 3 sec
    Functions.clear()

    text="The captain now leaves you and your team.\nYou are now in the arsenal and the following weapons are available."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print()
    Global.rest(1) 
    print()


    Functions.arsenal()
    print()
    text="All set commander? Let's dive into this mystery..."
    for i in text: #loop to print text letter by letter
        print(i,end="",flush=True)
        Global.rest(0.1)
    print()
    Global.rest(3) # clear text after 3 sec
    Functions.clear()


    '''
    Game plot
    '''
    Global.initialise_health()
    Global.initialise_score()

    #list_functions=[Functions.sea_snake,Functions.shark,Functions.ocean_current,Functions.team_mate,Functions.sensor,Functions.keypad,Functions.tap,Functions.journal,Functions.split,Functions.cell3,Functions.chooseInput,Functions.box2,Functions.chooseShape,Functions.win]


    while True:
        x=Functions.start()
        if x==1:
            x=Functions.sea_snake()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.shark()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.ocean_current()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break
        
        if x==1:
             Functions.clear()
             x=Functions.team_mate()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
             Functions.clear()
             x=Functions.sensor()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.keypad()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.tap()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.journal()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.split()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.cell3()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
              Functions.clear()
              x=Functions.chooseInput()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.box2()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            x=Functions.chooseShape()
        elif x==0:
            Functions.clear()
            Functions.loss()
            break

        if x==1:
            Functions.clear()
            Functions.win()
            break
        elif x==0:
            Functions.clear()
            Functions.loss()
            break
        
        break
