#----------------------------------------------------------------------------------------------------------------------------------------

#                                                     BATTLESHIP GAME (ASSIGNMENT 1)

#----------------------------------------------------------------------------------------------------------------------------------------
# importing modules
import random
import os
import sys            # to use module's exit() funtion when game over

#----------------------------------------------------------------------------------------------------------------------------------------

# VARIABLES
DIMENSION = 10        # constant variable for the size of the board (square) i.e. 10x10 grid
SHIP_SIZE = 4         # constant variable for the size of the ship i.e. 4 cells

board = []            # list for storing the board
ship = []             # list for storing ship coordinates and verifying hit or miss

col = ['A','B','C','D','E','F','G','H','I','J']   # column labels
row = ['0','1','2','3','4','5','6','7','8','9']   # row labels

guesses = 0           # stores number of guesses i.e. final score
n = 0                 # stores number of ships hit

#-----------------------------------------------------------------------------------------------------------------------------------------

print()
print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
print()

# printing the 10x10 grid/table with column and and row labels
print("     " + "   ".join(col))
print("   " + "+---" * DIMENSION + "+")
for x in range(DIMENSION):
    board.append([" "] * DIMENSION) 
num=0             
for cols in board:
    print(" " + str(num) + " " + "| "+" | ".join(cols) + " |")
    print("   " + "+---" * DIMENSION + "+")
    num+=1

print()
print("Instructions: Your goal is to take down all 4 battleships in least attempts!")
print("              If you miss the ship - #")
print("              If you hit the ship - X")

#----------------------------------------------------------------------------------------------------------------------------------------

# placing the ship's co-ordinates (hidden from user) either horizontally or vertically

orientation_final = random.randint(0, 1)     # to randomly get horizontal (0) or vertical (1)

#----------------------------------------------------------------------------------------------------------------------------------------

# HORIZONTAL CASE            # HORIZONTAL CASE              # HORIZONTAL CASE            # HORIZONTAL CASE          # HORIZONTAL CASE

#----------------------------------------------------------------------------------------------------------------------------------------

if orientation_final == 0:       # 0 implies Horizontal here

    # 10x10 duplicate board for ship
    ("     " + "   ".join(col))
    ("   " + "+---" * DIMENSION + "+")
    for x in range(DIMENSION):
        ship.append([" "] * DIMENSION)       # appending into ship[] 
    numship=0
    for cols in ship:
        (" " + str(numship) + "| "+" | ".join(cols)+" |")
        ("   " + "+---" * DIMENSION + "+") 
        numship+=1

    # storing ship's consecutive coordinates in "HORIZONTAL" case
    ship_row1 = random.randint(0, 9)         # using random function to get first row
    ship_col1 = random.randint(0, 6)         # using random function to get second column until 6 to ensure ship doesn't extend 
                                             # beyond the dimension as ship size is 4
    ship_col2 = ship_col1+1                  # storing next consective coordinate
    ship_col3 = ship_col1+2                  # storing next consective coordinate
    ship_col4 = ship_col1+3                  # storing next consective coordinate

    # four correct ship coordinates, stores 'X' to display when hit (correct guess from player)
    ship[ship_col1][ship_row1] = 'X'         
    ship[ship_col2][ship_row1] = 'X'
    ship[ship_col3][ship_row1] = 'X'
    ship[ship_col4][ship_row1] = 'X'


    # loops until the player hits all the four ships
    while n != 4:

        print()         # extra empty line for spacing

        target = input("Enter coordinate to target (e.g. A1): ")      # asks the player to guess the coordinates of ship
        target_list = list(target)                                    # converts player's input to list e.g. A1 ---> ['A', '1']  

        # to check if entered coordinate is valid or not:
            # condition 1 : length of list must be two i.e. row and column values
            # condition 2 : column ASCII values must lie between 65 (A) and 74 (J)
            # condition 3 : row values must lie in list col between 0 to 9 
        if (len(target_list)==2) and (ord(target_list[0])>=65 and ord(target_list[0])<=74) and (target_list[1] in ['0','1','2','3','4','5','6','7','8','9']):
            
            os.system("cls")        # clear screen in windows OS

            col_num = ['A','B','C','D','E','F','G','H','I','J'].index(target_list[0])    # storing index/position of targeted column
            row_num = ['0','1','2','3','4','5','6','7','8','9'].index(target_list[1])    # storing index/position of targeted row 
            

            # checking for a hit i.e if first targeted coordinate matches the ship coordinates
            if row_num == ship_row1 and col_num == ship_col1:
                
                board[ship_row1][ship_col1] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3 = 0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n == 4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking for a hit i.e if second targeted coordinate matches the ship coordinates
            elif(row_num == ship_row1 and col_num == ship_col2):
                
                board[ship_row1][ship_col2] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3 = 0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n == 4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking for a hit i.e if third targeted coordinate matches the ship coordinates
            elif(row_num == ship_row1 and col_num == ship_col3):
            
                board[ship_row1][ship_col3] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3 = 0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n == 4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking for a hit i.e if fourth targeted coordinate matches the ship coordinates
            elif(row_num == ship_row1 and col_num == ship_col4):
                
                board[ship_row1][ship_col4] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3 = 0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n == 4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over
                
            # checking if the entered coordinate is repeated / already guessed
            elif(board[row_num][col_num] == '#'):

                os.system("cls")     # clear screen windows OS
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()  
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num2=0
                for cols in board:
                    print(" " + str(num2) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num2+=1
                guesses+=1
                print()
                print("You've already guessed it!")
                
            # checking for a miss i.e. if entered coordinate is wrong
            elif(board[row_num][col_num] != '#'):
                    
                board[row_num][col_num] = '#'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()    
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num2=0
                for cols in board:
                    print(" " + str(num2) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num2+=1
                guesses+=1
                print()
                print("You missed the ship! Try Again.")
        else:
            print()
            print("Please re-enter a valid coordinate!")
            print()

#----------------------------------------------------------------------------------------------------------------------------------------

# VERTICAL CASE            # VERTICAL CASE             # VERTICAL CASE               # VERTICAL CASE               # VERTICAL CASE

#----------------------------------------------------------------------------------------------------------------------------------------

elif orientation_final == 1:        # 1 implies vertical

    # 10x10 duplicate board for ship
    ("   " + "   ".join(col))
    ("   " + "+---" * DIMENSION + "+")
    for x in range(DIMENSION):
        ship.append([" "] * DIMENSION)
    numship=0
    for cols in ship:
        (" " + str(numship) + " " + "| "+" | ".join(cols)+" |")
        ("   " + "+---" * DIMENSION + "+")
        numship+=1

    # storing ship's consecutive coordinates in "VERTICAL" case
    ship_row1 = random.randint(0, 6)         # using random function to get first row until 6 to ensure ship doesn't extend 
                                             # beyond the dimension as ship size is 4
    ship_col1 = random.randint(0, 9)         # using random function to get second column
    ship_row2 = ship_row1+1                  # storing next consective coordinate
    ship_row3 = ship_row1+2                  # storing next consective coordinate
    ship_row4 = ship_row1+3                  # storing next consective coordinate

    # four correct ship coordinates, stores 'X' to display when hit (correct guess from player)
    ship[ship_col1][ship_row1] = 'X'
    ship[ship_col1][ship_row2] = 'X'
    ship[ship_col1][ship_row3] = 'X'
    ship[ship_col1][ship_row4] = 'X'


#----------------------------------------------------------------------------------------------------------------------------------------

    # loops until the player hits all the four ships
    while n != 4:

        print()        # extra empty line for spacing
        target = input("Enter coordinate to target (e.g. A1): ")       # asks the player to guess the coordinates of ship
        target_list = list(target)                                     # converts player's input to list e.g. A1 ---> ['A', '1']  

        # to check if entered coordinate is valid or not:
            # condition 1 : length of list must be two i.e. row and column values
            # condition 2 : column ASCII values must lie between 65 (A) and 74 (J)
            # condition 3 : row values must lie in list col between 0 to 9 
        if (len(target_list)==2) and (ord(target_list[0])>=65 and ord(target_list[0])<=74) and (target_list[1] in ['0','1','2','3','4','5','6','7','8','9']):
            
            os.system("cls")      # clear screen in windows OS

            col_num = ['A','B','C','D','E','F','G','H','I','J'].index(target_list[0])     # storing index/position of targeted column
            row_num = ['0','1','2','3','4','5','6','7','8','9'].index(target_list[1])     # storing index/position of targeted row 
            

            # checking for a hit i.e if first targeted coordinate matches the ship coordinates
            if row_num == ship_row1 and col_num == ship_col1:
                
                board[ship_row1][ship_col1] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3=0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n==4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking for a hit i.e if second targeted coordinate matches the ship coordinates
            elif(row_num == ship_row2 and col_num == ship_col1):
                
                board[ship_row2][ship_col1] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3=0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n==4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

             # checking for a hit i.e if third targeted coordinate matches the ship coordinates
            elif(row_num == ship_row3 and col_num == ship_col1):
            
                board[ship_row3][ship_col1] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3=0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n==4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking for a hit i.e if fourth targeted coordinate matches the ship coordinates
            elif(row_num == ship_row4 and col_num == ship_col1):
                
                board[ship_row4][ship_col1] = 'X'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                # printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num3=0
                for cols in board:
                    print(" " + str(num3) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num3+=1
                n+=1
                guesses+=1
                print()
                print("Congratulations!", str(n), "ships down!")
                if n==4:
                    print("Game Over! You sank all the ships!")
                    print("Your score (no. of guesses) is " + str(guesses))
                    sys.exit()    # to terminate the program when game over

            # checking if the entered coordinate is repeated / already guessed
            elif(board[row_num][col_num] == '#'):

                os.system("cls")     # clear screen windows OS
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                #printing the updated board
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num2=0
                for cols in board:
                    print(" " + str(num2) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num2+=1
                guesses+=1
                print()
                print("You've already guessed it!")
                
            # checking for a miss i.e. if entered coordinate is wrong    
            elif(board[row_num][col_num] != '#'):
                    
                board[row_num][col_num] = '#'
                print()
                print("        BATTLESHIP GAME (ASSIGNMENT 1)")       # extra spaces for centering the text with respect to the board
                print()
                #printing the updated board    
                print("     " + "   ".join(col))
                print("   " + "+---" * DIMENSION + "+")
                num2=0
                for cols in board:
                    print(" " + str(num2) + " " + "| " + " | ".join(cols) + " |")
                    print("   " + "+---" * DIMENSION + "+")
                    num2+=1
                guesses+=1
                print()
                print("You missed the ship! Try Again.")
        else:
            print()
            print("Please re-enter a valid coordinate!")
            print()    



#------------------------------------------------- END OF PROGRAM -----------------------------------------------------------------------