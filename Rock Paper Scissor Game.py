import random

def RPS_Game(nop):
    CP=0
    UP=0
    d={1:"Rock",2:"Paper",3:"Scissor"}
    while CP!=nop and UP!=nop:
        Comp_guess=random.choice(["Rock","Paper","Scissor"])
        User_guess=int(input("Enter 1 for Rock, 2 for Paper or 3 for Scissor: "))
        if (Comp_guess=="Rock" and User_guess==2) or (Comp_guess=="Paper" and User_guess==3) or (Comp_guess=="Scissor" and User_guess==1):
            print("Oh!",d[User_guess],"beats",Comp_guess,". You won this round!")
            UP+=1
        elif (Comp_guess=="Paper" and User_guess==1) or (Comp_guess=="Scissor" and User_guess==2) or (Comp_guess=="Rock" and User_guess==3):
            print("Yes!",Comp_guess,"beats",d[User_guess],". I won this round!")
            CP+=1
        else:
            print("Oh we both picked",Comp_guess,". This round is a draw!")
        print("Points are:")
        print("User Points: ",UP)
        print("Computer Points: ",CP)
        print()
    if CP==nop:
        print("I won the game!!!")
    elif UP==nop:
        print("You won the game!!!")
        
nop=int(input("Welcome to rock paper scissors!!! Enter number of points required to win: "))
print()
RPS_Game(nop)
