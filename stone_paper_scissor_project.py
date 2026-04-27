import random
game=["rock","paper","scissor"]

# It is the code for player vs player

def player(p1,p2):
    found=False
    while found==False:
        player=input(f"{p1} Your turn press enter")
        if player=="":
            move1=random.choice(game)
            print(f"{p1} move",move1)
            found=True
        else:
            print("invalid press choose again")
            found=False
        player=input(f"{p2} Your turn press enter")
        if player=="":
            move2=random.choice(game)
            print(f"{p2} move",move2)
            found=True
        else:
            print("invalid press choose again")
            found=False
        if move1==move2:
            print("it's a tie!")
        elif (move1=="paper" and move2=="rock")or(move1=="rock" and move2=="scissor")or(move1=="scissor" and move2=="paper"):
            print(f"{p1} you won the round !")
        else:
            print(f"{p2} you won the round!")





#It is the code for player vs computer

def comp(p):
    computer_choice=random.choice(game)
    your_choice=input("Enter your choice (rock,paper,scissor):")
    if your_choice.lower()==computer_choice:
        print("it's a tie !")
    elif (your_choice.lower()=="paper" and computer_choice=="rock")or(your_choice.lower()=="rock" and computer_choice=="scissor")or(your_choice.lower()=="scissor" and computer_choice
        =="paper"):
            print(f"{p} you won the round !")
    else:
        print("Computer choice :",computer_choice)
        print("computer won the round!")





# This is the main program for user


def user():
    found=False
    while found==False:
        print("GAME WILL START WHEN YOU CHOOSE \n CHOOSE ONLY NUMBER TO START WITH")
        info=int(input("1.player vs player\n2.player vs computer\n"))
        if info==1:
            p1=input("player1:")
            p2=input("player2:")
            found=True
            player(p1,p2)
        elif info==2:
            p=input("name of player:")
            comp(p)
            found=True
        else:
            print("invalid choice\nchoose again ")
            found=False

while True:
    user()
    choice=input("You want to play again yes or no :")
    if choice.lower()!="yes":
        print("___Exited____")
        break