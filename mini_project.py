#guess the  random number

import random 
target =random.randint(1,50)
while True:
    userchoice=input("Guess the target or Quit(Q):")
    if(userchoice=="Q"):
        break

    userchoice=int(userchoice)
    if(userchoice==target):
        print("Correct Guess!!!")
        break
    elif(userchoice<target):
        print("Sorry...Take a bigger guess")
    else:
        print("sorry...Take a smaller guess")

print("*********GAME OVER*********")           


