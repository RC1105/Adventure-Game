from time import *
import Global


def Terrorist():
   # name=input("ENTER YOUR NAME:")
    name=Global.name
    text="Hey!",name," Welcome to adventure Game\n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()
    text="You will get 2-3 options for every task you get \n choose them smartly or else you might end up losing \n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()

    inst1=input( "Unfortunately, terrorists have entered the 3 floor building you are in!! PRESS ENTER TO CONTINUE\n \n")
    text="Try to get off the building as soon as possible\n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()
    print('\n')
    text="You are currently on the second floor \n  \n You are all set to begin \n \n Good Luck ", name,"\n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()
    #question1
    def q1(ans1,ans2,ans3):
        global points, distance, flag
        points=0
        distance=0
        flag=0
        global lst
        lst=[]
        lst.append(ans1)
        lst.append(ans2)
        lst.append(ans3)
        return lst
        points=points+50
    text="Choose any 3 items you might need for evasion: \n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()
    print("A. Rope \n B. mobile \n C. axe \n D. torch \n E. knife \n F. water bottle \n G. Bunch of keys \n")
    opt1=input("Choose first item type A or a for rope B or b for mobile etc: ")
    opt2=input("Choose second item type A or a for rope B or b for mobile etc: ")
    opt3=input("Choose third item type A or a for rope B or b for mobile etc: ")
    q1(opt1,opt2,opt3)


    print('\n')
    #question2
    def q2(ans):
        global points, distance, flag
        if ans=='A' or ans=='a':    
            if "c"  in lst or 'C' in lst:
                text="Amazing the door is open now....\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                points=points+50
                distance=distance+25
                text="You have covered ",distance,"m\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
            else:
                text="You don't have an axe...Game over\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        elif ans=='b' or ans=='B':
            if "G" in lst or 'g' in lst:
                text="Amazing the door is open now....\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                points=points+50
                distance=distance+25
                text="You have covered ",distance,"m\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
            else:
                text="You don't have keys.... Game over \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        else:    
            text="Game Over... you couldn't open door \n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()

    text="we are off the mark but what's this...A LOCKED DOOR! \n"
    for i in text:
        print(i,end='',flush=True)
        Global.rest(0.1)
    print()
    print("A. Use axe to break the lock & open the door \n B. place a random key\n ")
    b=input("what will you choose? :")
    q2(b) 
    print("\n")
    if flag==1:
        #question3
        def q3(ans):
            global points, distance, flag
            if ans=='B' or ans=='b':   
                text="You are safe the terrorist went away...looks like it isn't safe to go there back \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+50
                print("You have covered ",distance,"m")
            else:
                text="Game Over... You tried to kill a terrorist using a knife come on.. he is a terrorist he's well equipped with guns and grenades\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        print("\n")
        text="You can see a terrorist monitoring the CCTV  \n "
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("A. Attack the terrorist using knife \n B. Run away and get into the nearest room \n")
        c=input("what will you do? :")
        q3(c)
    print("\n")
    if flag==2:
        #question4
        def q4(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':    
                text="BOMB DIFFUSED SUCCESSFULLY...Well done mate \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+100
                print("You have covered ",distance,"m")
            else:
                text="Game Over... Bomb explodes \n "
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="This room looks strange...\n There's nothing kept as such\n there's a window Hey what's that.. Oh no....it's a time bomb \n There is a bomb adjacent to the window"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print(" \n A. Try to diffuse it \n B. Run away \n")
        d=input("what will you do? :")
        q4(d)
    print("\n")
    if flag==3:
        #question5
        def q5(ans):
            global points, distance, flag
            if ans=='a' or ans=='A':    
                text="BOOM...Oh no!!...the Fire Broke Out but we are safe  \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+200
                
                print("You have covered ",distance,"m\n")
            else:
                text="Game Over... Fire Broke Out and you're dead \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="Also there is a closed door which looks greasy What's this on the floor... Looks like an oil spill"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("\n A. Run away..it can be deadly \n B. Ignore it's just a coincidence \n")
        e=input("what will you do? :")
        q5(e)
    print("\n")
        
    if flag==4:
        #question6
        def q6(ans):
            global points, distance, flag
            if ans=='B' or ans=='b':    
                text="Well done we should never use elevator when fire is on!! \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+5
                
                text="You have covered",distance,"m\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
            else:
                text="Game Over... We should never use elevator when fire is there\n You are dead \n "
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="Fire alarm is on now you must rush now and switch the floor\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print(" \n A. Use an elevator \n B. use Staircase \n")
        f=input("what will you choose? :")
        q6(f)
    print("\n")
    if flag==5:
        d5=5
        #question7
        def q7(ans):
            global points, distance, flag
            if ans=='b' or ans=='B':
                text="You have reached the Ground floor \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()

            else:
                text="You have reached the 2nd floor\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
            flag=flag+1
            points=points+50
            distance=distance+50
            print("You have covered",distance,"m\n")
        text="You can now see the staircase...\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print(" \n A. Upstairs i.e. 2nd floor \n B. Downstairs i.e. Ground Floor\n")
        g=input("where to go? :")
        q7(g)
        print("\n")
        print("\n")
        text="This floor looks similar to the previous floor\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()


    if flag==6:
        d6=50
        #question8
        def q8(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':    
                text="Well done!! One should never take risks when fire's on \n "
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+50
                text="You have covered ",distance,"m\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                text="\nFIRE EXTINGUISHED \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
            else:
                text="Game Over... EXPLOSION...One should never risk fire..  \n "
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="No idea how far is the  exit \n There's a fire extinguisher on the wall...The fire doesn't look that intense we can easily extinguish it \n "
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("A. Use fire extinguisher; can't take risks with fire, it can intensify \n B. take a risk and go ahead\n")
        h=input("what will you do? :")
        q8(h)
        
    print("\n")
    if flag==7:
        #question9
        def q9(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':
                if 'D' in lst or 'd' in lst:
                    text="Good decision....You thought of being careful and reduce risk.. \n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
                    flag=flag+1
                    points=points+50
                    distance=distance+50
                    text="You have covered ",distance,"m\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
                else:
                    text="Game over.. you don't have torch\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
            elif ans=='B' or ans=='b':
                if 'B' in lst or 'b' in lst:
                    text="Good decision....You thought of being careful and reduce risk.. \n"
                    for i in text:
                        print(i,end='')
                    flag=flag+1
                    points=points+50
                    distance=distance+50
                    text="You have covered ",distance,"m\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
                else:
                    text="Game over...You don't have mobile\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
            else:
                text="Game Over.... You went to dark room without torch, terrorists had plotted this dark room plan to kill you...\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        print("")
        text="As the corridor ends, you can see 3 rooms of which only one is opened.. Let's get in \n Now you enter a DARK ROOM, where you have no light source.\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print(" A. Use Torch \n B. Use flashlight of mobile \n C. get in without source of light \n"  )
        i=input("what will u do? :")
        q9(i)
    print("\n")
    if flag==8:
        #question10
        def q10(ans):
            global points, distance, flag
            if ans=='b' or ans=='B':   
                text="Smart decision...picking a gun lying on the floor directly wasn't safe... \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+50
                text="You have covered ",distance,"m\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
            else:
                text="BOOM.....Bomb explodes...gun lying on the floor was a trap by terrorists... Game over \n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="On your way,you see a gun AK-47 lying on the floor.\n "
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("A. Pick the gun \n B. Don't pick and go ahead \n")
        j=input("What seems as a better idea to you? :")
        q10(j)

    print("\n")
    if flag==9:
        #11 and 12th question
        def answer12():
            global points, distance, flag
            text="Over to Agent X \n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
            text="Agent X:  Hey mate.. there's no time to introduce ourselves I'm here to help you out\n Follow me fast...come on!! \n \n \n Agent has helped you reach a place which looks peaceful \n \n \nAgent X: I have some work.. you just go straight\n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
            text="Good Luck mate\n \n \n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
            text="with the help of Agent you have reached an open space...Finally a relief\n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
            flag=flag+1
            points=points+50
            distance=distance+250
            text="You have covered ",distance,"m\n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
        def answer12b():
            global points, distance, flag
            text="Was that person lucky charm?? as when you hid from him \n \n You see a really unique place let's go ahead and see \n Looks like an escape tunnel heading above ..\n You have reached an open space.. Finally a releif\n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
            flag=flag+1
            points=points+50
            distance=distance+250
            text="You have covered",distance,"m\n"
            for i in text:
                print(i,end='',flush=True)
                Global.rest(0.1)
            print()
        def q11(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':    
                text="Looks like he isn't a terrorist...\n He is Agent X \n He says he has an escape plan ready\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                q12=input("Do you wish to trust him? A. YES B. NO")
                if q12=="A" or q12=="a":
                    answer12()
                else:
                    text="It's good not to trust anyone in these harsh situations...\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
                    answer12b()
                points=points+50
            else:  
                text="Well looks like he wasn't a terrorist he was an agent..\n No worries we have found a great route to escape\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                answer12b()
        text="Let's get out of here..\n Hey! what's behind?? looks like you are being followed by SOMEONE.\n "  
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("A. To check who is that person \n B. Hide from him\n")
        k=input("What's your immediate step?")
        q11(k)
    print("\n")
    if flag==10:
        #question14
        def q14(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':    
                if  'A' in lst or 'a' in lst :
                    text="Yeah rope!! no alternative could have been better\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()
                    flag=flag+1
                    points=points+50
                    distance=distance+50
                    text="You have covered ",distance,"m\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()

                else:
                    
                    text="You don't have rope.. Game over\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()

            else:
                text="Game over\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()

        #question 13
        def q13(ans):
            global points, distance, flag
            if ans=='A' or ans=='a':    
                text="You've reached the terrace!!\n What a BREEZE \n There's an external staircase \n Let's go to the ground floor \n" 
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                print("A. YES \n B. NO\n")
                inp=input("do you wish to go" )
                if inp=='A' or inp=='a':
                    flag=flag+1
                    points=points+50
                    distance=distance+200
                    text="You have covered ",distance,"m\n"
                    for i in text:
                        print(i,end='',flush=True)
                        Global.rest(0.1)
                    print()

                else:
                    flag==11
            else:
                text="You've reached the terrace!! \n What a BREEZE \n But What?? there is no way to go down, rope is the only possible option ..\n"  
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                print("A. Use rope \n B. Surrender as I don't have rope\n")
                n=input("What seems as a better idea to you? :")
                q14(n)
                
        text="Looks like bad times are about to get over... But what's this...\n There are two directions."
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print("\n A. left \n B. right\n")
        m=input("Where to go? :")
        q13(m)
    print("\n")
    if flag==11:
        def q15(ans):
            global points, distance, flag
            if ans=='B' or ans=='b':
                text="Good move...Not a good day to trust unknown vehicles.. Could have been their bad technique\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
                flag=flag+1
                points=points+50
                distance=distance+170
            else:
                text="Game Over...terrorists had planted bombs in all vehicles in parking lot to kill people trying to escape...\n"
                for i in text:
                    print(i,end='',flush=True)
                    Global.rest(0.1)
                print()
        text="You have reached the Ground Floor \n Parking lot it is!! \n"
        print("A. Choose a car parked in parking lot of building \n B. Running away from the building\n")
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        o=input("what will u do? :")
        q15(o)
    print('\n \n \n \n')
    if flag==12:
        text="You have completed the game!!\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text="Well played ",name
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text=name,"your score is:",points
        print("\n")
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text="Total distance travelled is ",distance
        print("\n")
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text="It is the maximum points scored and distance travelled by anyone till date"
        print("\n")
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
    else:
        text= "Better luck next time \n Well played ",name
        print('\n')
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text=name," your score is:",points
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
        print('\n')
        text="Total distance travelled is ",distance,"m\n"
        for i in text:
            print(i,end='',flush=True)
            Global.rest(0.1)
        print()
