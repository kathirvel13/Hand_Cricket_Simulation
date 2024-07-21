import random

print("""\t\t\t\tWelcome to Hand Cricket Simulation (Odd or even)
\t\t\t\t************************************************
Rules to Play: 
\t1. All your input numbers should be between 1 to 6.
\t2. The computer will also select a number.
\t3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
\t   If the number selected by you and computer is same, then you will lose your wicket.
\t4. While bowling, if the number selected by you and computer is different, then computer's number will add to its runs.
\t   If the number selected by you and computer is same, then the computer will lose its wicket.
\t5. Both the computer as well as the player gets one wicket.
\t6. Batting or bowling is chosen by toss.
\t7. The player continues to bat or bowl until you lose the wicket.
\t8. The player with maximum runs wins.\n""")

def gameinput(input_text):
    # Function to get valid input from user
    while True:
        inputno = int(input(input_text))
        if inputno >= 1 and inputno <= 6:
            return inputno
        else:
            print("Enter a valid input number!\n")

def playtoss():
    option = gameinput("Choose Heads (1) or Tails (2): ")
    randHT = random.randint(1,2)
    
    if randHT == 1:
        print("Heads!")
    else:
        print("Tails!")
    
    if randHT == option:
        print("You won the toss!")
        play = gameinput("Choose Bat (1) or Bowl (2): ")
        if play == 1:
            print("You are the batsman!")
        elif play == 2:
            print("You are the bowler!")
    else:
        print("Computer won the toss!")
        play = random.randint(1,2)
        if play == 1:
            print("Computer chooses to bowl!")
        elif play == 2:
            print("Computer chooses to bat!")
    print()
    return play

def batting():
    global pscore
    global cscore
    ballcount = 0
    while True:
        playeropt = gameinput("Choose any number from 1 to 6: ")
        compopt = random.randint(1,6)
        print(f"Computer plays {compopt}")
        if playeropt == compopt:
            print(f"Player loses his wicket. Score - {pscore}. Number of turns played - {ballcount}.\n")
            return "pout"
        else:
            pscore += playeropt
            ballcount += 1
            print(f"Player's score is {pscore}")
        print()

def bowling():
    global cscore
    global pscore
    ballcount = 0
    while True:
        playeropt = gameinput("Choose any number from 1 to 6: ")
        compopt = random.randint(1,6)
        print(f"Computer plays {compopt}")
        if playeropt == compopt:
            print(f"Computer lost its wicket. Score - {cscore}. Number of turns played - {ballcount}.\n")
            return "cout"
        else:
            cscore += compopt
            ballcount += 1
            print(f"Computer's score is {cscore}")
        print()
            
pscore = 0
cscore = 0

# gamestate is either batting (1) or bowling (2) for the player
gamestate = playtoss()

if gamestate == 1:
    batting()
    # changing gamestate
    gamestate = 2
    print("Now its your Bowling turn.")
else:
    bowling()
    # changing gamestate
    gamestate = 1
    print("Now its your Batting turn.")

if gamestate == 1:
    batting()
else:
    bowling()
    
if pscore > cscore:
    print("Player won the match! Congratulations!")
elif pscore < cscore:
    print("Computer won the match. Better luck next time!")
elif pscore == cscore:
    print("It's a tie! well played.")