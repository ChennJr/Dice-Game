import random
import time
import sys

PASSWORD = "1234" # Game password
passwordAttempts = 0 
round = 1 
decision_to_view_rules = ""  # Does the player want to view the rules and/or scoreboard
decision_to_view_scoreboard = ""
player_1_total_points = 0
player_1_dice_rolled = 0
player_2_total_points = 0
player_2_dice_rolled = 0
gameProgress = "ONGOING"

def remove(string): # removes blank spaces in a string
    return string.replace(" ", "")

def print_dice_faces(dice_numbers_rolled):
    dice_faces = ["", # index 0 doesn't have a face
                "[     ]\n[  0  ]\n[     ]", # index 1 
                "[0    ]\n[     ]\n[    0]", # index 2
                "[0    ]\n[  0  ]\n[    0]", # index 3
                "[0   0]\n[     ]\n[0   0]", # index 4
                "[0   0]\n[  0  ]\n[0   0]", # index 5
                "[0   0]\n[0   0]\n[0   0]", # index 6
                ] 
    faces = [dice_faces[x].splitlines() for x in dice_numbers_rolled]
    for line in zip(*faces):
        print(*line)
    
def diceRoll(num_of_dice_to_roll):
    
    dice_numbers_rolled = [random.randint(1,6) for x in range(num_of_dice_to_roll)] # outputs a list to show which numbers rolled i.e [2, 6] (rolled a 2 and 6)
    print(f"Die 1: You rolled a {dice_numbers_rolled[0]}")
    print(f"Die 2 : You rolled a {dice_numbers_rolled[1]} \n")
    print_dice_faces(dice_numbers_rolled)
    print("\n")

    points_added = dice_numbers_rolled[0] + dice_numbers_rolled[1]

    if (points_added % 2) == 0: # if the points added is even
        points_added = points_added + 10

    else:
        points_added = points_added - 5

    if dice_numbers_rolled[0] == dice_numbers_rolled[1]:
        print("You rolled a double, you get a bonus roll")
        bonusDie = random.randint(1,6)
        time.sleep(2)
        print(f"Bonus Die: You rolled a {bonusDie} \n")
        print_dice_faces([bonusDie])
        print("\n")

        points_added = points_added + bonusDie

    return points_added

def slowPrint(text, delay=0.025):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.025)

def exitMenu():
    exitMenu = remove(input())
    if exitMenu == "":
        print("\033c", end='')
    
    else:
        pass

def viewScoreboard():
    score_list = [] # creates array to store sublists, creating a 2d array
  
    with open('scoreboard.txt', 'r') as f: # opens scoreboard.txt and reads the file lines, 'with' automatically closes file
        for line in f.readlines(): # loop to store each word detected in each line of the txt file by split() function
            word = line.split() # stores each word seperated by spaces in a single line as an array (list), from the txt file, in a variable ie. [Jackson's, Score:, 12]
        
            score_list.append(word) # stores words in single line from variable into the array (list), sorted by line ie. [[Jackson's, Score:, 12], [Alex's, Score:, 13], [Eric's, Score:, 14]]...
                                                                                        # words in line 1 of the txt file ^                         ^                     ^         
                                                                                                                  # words in line 2 of the txt file ^                     ^
                                                                                                                                        # words in line 3 of the txt file ^
      
        score_list.sort(key = lambda score_list: int(score_list[2]), reverse=True) # sorts list by indexing value [2] of each sublist which is the score ie. [Jackson's, Score:, 12], 'reverse=True sorts it descending whereby, default is acsending'                                                                                                                                  ^         ^       ^
                                                                                                                                     # index value [0] ^         ^       ^
                                                                                                                                               # index value [1] ^       ^
                                                                                                                                                       # index value [2] ^
  
    for x in range(0,5): # Loop to display top 5 scores on leaderboard
        print (score_list[x][0] + " " + score_list[x][1] + " " + score_list[x][2]) # outputs leaderboard in format 'Player_name's, Score:, score_integer'

def rollCheck(player, player_1_total_points, player_2_total_points):
    rollCheck = remove(input())
    if rollCheck == "":
        if player == "1":
            player_1_dice_rolled = diceRoll(2)
            print(f"Points added: {player_1_dice_rolled}")
            player_1_total_points = player_1_dice_rolled + player_1_total_points
            if player_1_total_points < 0:
                player_1_total_points = 0
            rollCheck = " "
            return player_1_total_points

        else: 
            player_2_dice_rolled = diceRoll(2)
            print(f"Points added: {player_2_dice_rolled}")
            player_2_total_points = player_2_dice_rolled + player_2_total_points
            if player_2_total_points < 0:
                player_2_total_points = 0
            rollCheck = " "
            return player_2_total_points
    else:
        pass

def startRound(player, round, player_1_total_points, player_2_total_points):
    print(f"Round: {round} \n")
    time.sleep(1.5)
    
    if player == "1":
        slowPrint("Player 1 turn: \n")
        time.sleep(1)
        slowPrint("Press ENTER to roll \n")
        player_1_total_points = rollCheck("1", player_1_total_points, player_2_total_points)
        print(f"Total points: {player_1_total_points}")

        time.sleep(3)
        print("\033c", end='')
    

    else:
        slowPrint("Player 2 turn: \n")
        time.sleep(1)
        slowPrint("Press ENTER to roll! \n")
        player_2_total_points = rollCheck("2", player_1_total_points, player_2_total_points)
        print(f"Total points: {player_2_total_points}")
    
    time.sleep(3)
    print("\033c", end='') 
    
    if player == "1":
        return player_1_total_points

    else:
        return player_2_total_points

def saveScore(player):
    if player == "1":
        with open("scoreboard.txt", "a") as scoreboard_file:
            scoreboard_file.write(f"{player_1_first_name}'s Score: {str(player_1_total_points)} \n")
    
    else:
        with open("scoreboard.txt", "a") as scoreboard_file:
            scoreboard_file.write(f"{player_2_first_name}'s Score: {str(player_2_total_points)} \n")

def checkWinner(player):
    if player == "1":
        print(f"Player 1 has won with a total of {player_1_total_points} points")
        saveScore("1")

    else:
        print(f"Player 2 has won with a total of {player_2_total_points} points")
        saveScore("2")

def playAgain():
    playAgain = remove(input().upper())
    while playAgain != "Y" and playAgain != "N":
        slowPrint("Would you like to play again? Y or N \n")
        playAgain = remove(input().upper())
    
    if playAgain == "Y":
        print("\033c", end='')
        return "Yes"
    
    else:
        return "No"
        


slowPrint("These details will be needed to verify that you are authorised players")
time.sleep(2.5)
print("\033c", end='')

slowPrint("Player 1, what is your first name? \n")
player_1_first_name = input("")

slowPrint("What is your last name? \nPress ENTER to skip if your username does not contain your last name \n")
player_1_last_name = input("")

slowPrint("What year were you born? \nPress ENTER to skip if your username does not contain your birth year \n")

player_1_birth_year = input("")

if player_1_last_name == "" or player_1_birth_year == "":
    player_1_username = player_1_first_name.upper()

else:
    player_1_username = player_1_first_name[0].upper() + player_1_last_name.upper() + player_1_birth_year

slowPrint("Player 2, what is your first name? \n")
player_2_first_name = input("")

slowPrint("What is your last name? \nPress ENTER to skip if your username does not contain your last name \n")
player_2_last_name = input("")

slowPrint("What year were you born? \nPress ENTER to skip if your username does not contain your birth year \n")
player_2_birth_year = input("")

if player_2_last_name == "" or player_2_birth_year == "":
    player_2_username = player_2_first_name.upper()

else:
    player_2_username = player_2_first_name[0].upper() + player_2_last_name.upper() + player_2_birth_year

with open("players.txt", "r") as players:
    accounts = []
    for line in players.readlines():
        accounts.append(line.replace("\n", ""))
        
    if player_1_username in accounts and player_2_username in accounts:
        print(f"Welcome to Dice Game {player_1_first_name} and {player_2_first_name}!")

    elif player_1_username in accounts:
        print(f"{player_2_first_name} you are not an authorised user")
        quit()
    
    elif player_2_username in accounts:
        print(f"{player_1_first_name} you are not an authorised user")
        quit()

    else:
        print(f"{player_1_first_name} and {player_2_first_name}, both of you are not authorised players")
        quit()

slowPrint("Please enter the game password \n")
inputedPassword = input("")

while inputedPassword != PASSWORD: # password authentication
    print(f"Incorrect password, you have {3 - passwordAttempts} attempt(s) left")
    passwordAttempts += 1
    slowPrint("What is the password? \n")
    inputedPassword = input("")

    if passwordAttempts == 3:
        slowPrint("You have entered the incorrect password too many times!")
        quit()

print("Correct password!")
time.sleep(1)
print("\033c", end='')

while decision_to_view_rules != "Y" and decision_to_view_rules != "N":
    slowPrint("Would you like to see the rules and instrucitons? Y or N \n")
    decision_to_view_rules = remove(input().upper())

if decision_to_view_rules == "Y": # if player wants to display rules
    print("\033c", end='')
    print("------------------------------------------------------------------RULES------------------------------------------------------------------")
    print("1. You will role two 6-sided dices, your rolled total will be added to your score")
    print("2. If your rolled total is an even number: +10 additional points to your score")
    print("3. If your rolled total is an odd number: -5 points to your score")
    print("4. If you roll a double, roll one extra die: your rolled total is added to your score, rules 2. and 3. don't apply")
    print("5. Your score cannot go below 0")
    print("6. You take turns for 5 rounds, the person with the highest score at the end wins")
    print("7. If both users have the same score at the end of the 5 rounds, deathmatch occurs: keep rolling until someone gets a higher total score ")
    print("8. Winner's score is updated onto the scoreboard")
    print("------------------------------------------------------------------RULES------------------------------------------------------------------")
    slowPrint("Press ENTER to continue \n")
    exitMenu()

else:
    print("\033c", end='')

while decision_to_view_scoreboard != "Y" and decision_to_view_scoreboard != "N":
    slowPrint("Would you like to see the scoreboard? Y or N \n")
    decision_to_view_scoreboard = remove(input().upper())

if decision_to_view_scoreboard == "Y":
    viewScoreboard()
    slowPrint("Press ENTER to continue \n")
    exitMenu()

else:
    print("\033c", end='')

while gameProgress != "ENDED":
    while round != 6:
        player_1_total_points = startRound("1", round, player_1_total_points, player_2_total_points)
        player_2_total_points = startRound("2", round, player_1_total_points, player_2_total_points)
        round += 1
        continue

    if player_1_total_points > player_2_total_points:
        checkWinner("1")
        decision = playAgain()
        if decision == "Yes":
            round = 1
            player_1_total_points = 0
            player_2_total_points = 0
            continue
        else:
            slowPrint("Thanks for playing!")
            quit()

    elif player_1_total_points < player_2_total_points:
        checkWinner("2")
        decision = playAgain()
        if decision == "Yes":
            round = 1
            player_1_total_points = 0
            player_2_total_points = 0
            continue
        else:
            slowPrint("Thanks for playing!")
            quit()
    
    else:
        slowPrint("Both players are tied, entering deathmatch. Rounds will continue until a player is victorious \n")
        time.sleep(3)
        slowPrint("Good luck! \n")
        time.sleep(2)
        print("\033c", end='')

        while player_1_total_points == player_2_total_points:
            
            player_1_total_points = startRound("1", round, player_1_total_points, player_2_total_points)
            player_2_total_points = startRound("2", round, player_1_total_points, player_2_total_points)
            round += 1
            continue

        if player_1_total_points > player_2_total_points:
            checkWinner("1")
            decision = playAgain()
            if decision == "Yes":
                round = 1
                player_1_total_points = 0
                player_2_total_points = 0
                continue
            
            else:
                slowPrint("Thanks for playing!")
                quit()

        elif player_1_total_points < player_2_total_points:
            checkWinner("2")
            decision = playAgain()
            if decision == "Yes":
                round = 1
                player_1_total_points = 0
                player_2_total_points = 0
                continue
            
            else:
                slowPrint("Thanks for playing!")
                quit()    

   
