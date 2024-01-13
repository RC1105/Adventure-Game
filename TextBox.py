'''
This is the main program file
'''

import File1
import File2
import Global

print("WELCOME TO THE TEXT-BASED ADVENTURE GAME!")
print('\n\n')

Global.initialise_name()
Global.name=input('Enter Username: ')
print('\n\n')

print("Instructions:")
print("To input your choice and proceed in the story, please enter the corresponding number of your choice.")
print('\n')

print("1. Terrorist attack\n2. Underwater mission")

def choice():
    choice=int(input("Which game would you like to play? : "))
    print('\n\n')
    if choice==1:
        File2.Terrorist()
    elif choice==2:
        File1.Underwater()
    else:
        print("Incorrect input. Please enter the corresponding number of your choice.")
        print('\n')
        choice()

choice()
    
