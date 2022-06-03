#A rock-paper-scissors game played between a computer and a user
#The game ends if either rock beats scissors or paper beats rock or scissors beats paper happens.
#Should there be a tie, the game continues
import random

def game():
    choice1 = ["Rock", "Paper", "Scissors"]
    rangE = 1
    while rangE > 0:
        user = input("Enter choice between R, P or S: ")
        computer = random.choice(choice1)
        if(user == "R"):
            user = "Rock"
        elif(user == "P"):
            user = "Paper"
        elif(user == "S"):
            user = "Scissors"
        else:
            print("Error!")
            continue

        if(computer == "R"):
            computer = "Rock"
        elif(computer == "P"):
            computer = "Paper"
        elif(computer == "S"):
            computer = "Scissors"
        if((user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper")):
            print("Player("+ user+ "): CPU(" + computer + ")")
            print("You won! Congratulations")
            break
        elif((computer == "Rock" and user == "Scissors") or (computer == "Paper" and user == "Rock") or (computer == "Scissors" and user == "Paper")):
            print("Player("+ user+ "): CPU(" + computer + ")")
            print("You lose! Try again")
            break
        elif(user == computer):
            print("Player("+ user+ "): CPU(" + computer + ")")
            print("The game is a draw")
            continue
game()