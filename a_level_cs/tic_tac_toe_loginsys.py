# Lua is the superior programming language, Python scope indentations sucks bro
# most disgusting program i've ever made some shit in here just doesn't make sense 
import random
global usernameIndex 
global usernameNotFound
global ticTacToeCount 
global newUsername 

ticTacToeCount = 0 
usernameNotFound = True
usernamesFile = open("usernames.txt", "a")
passwordsFile = open("passwords.txt", "a")
usernamesFile.close()
passwordsFile.close()

choice = input("1. Login 2. Create an Account 3. See User Data 4. Quit (Please enter 1, 2, 3 or 4): ")
loggedIn = False 
accountMade = False
gameRunning = True
positionalArray = [" "] * 9
returnedToMenu = False 
quitted = False

def drawBoard(positionalArray): 
    for i in range(0, 9, 3): 
        print(f"{positionalArray[i]} | {positionalArray[i + 1]} | {positionalArray[i + 2]}")
        if i < 6:
            print("----------")
    
def aiMove(positionalArray): 
    while True: 
        randomNumber = random.randint(0, len(positionalArray)) - 1
        if positionalArray[randomNumber] == " ": 
            positionalArray[randomNumber] = "X" 
            break

def checkWinner(positionalArray):
    winCombinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Left diagonal
        [2, 4, 6]   # Right diagonal
    ]

    for combo in winCombinations:
        if positionalArray[combo[0]] == positionalArray[combo[1]] == positionalArray[combo[2]] != " ":
            winner = positionalArray[combo[0]]
            if winner == "O":
                return 1  # Player wins
            elif winner == "X":
                return 2  # AI wins
    
    return 0  # No winner yet

def getAmountOfWins(fileContents, username):
    if username[0:username.find('|')] == username[0:username.find('|')]:
        for content in fileContents:
            if content[0:content.find('|')] == username:
                equalSignIndex = content.find('=')
                slicedString = content[equalSignIndex:len(content)]
                wins = int(slicedString[1:slicedString.find('|')])
                return wins

    return 0 

def getAmountOfLosses(fileContents, username):
    if username[0:username.find('|')] == username[0:username.find('|')]:
        for content in fileContents:
            if content[0:content.find('|')] == username:
                equalSignIndex = content.find('=')
                slicedString = content[equalSignIndex + 1:len(content)]
                losses = int(slicedString[slicedString.find('=') + 1:len(content) - 1])

                return losses
    return 0 
def updateUserData(usernamesFile, passwordsFile, wins, losses, username, usernameFileContents, passwordFileContents, usernameIndex, checkWinner):
    if checkWinner == 1: # They have won!
        wins += 1
        wins = str(wins)
        losses = str(losses)

        for i in range(len(usernameFileContents)):
            userdataString = usernameFileContents[i]

            if userdataString == username:
                equalSignIndex = userdataString.find('=')
                
                # Closing the file because we're trying to write to it fr!
                usernamesFile.close()
                passwordsFile.close()
                
                usernamesFile = open("usernames.txt", "w") 
                passwordsFile = open("passwords.txt", "w")

                if userdataString == username:
                    if usernameIndex == j and username == usernameFileContents[usernameIndex] and password + "\n" == passwordFileContents[j]:
                        usernameFileContents[usernameIndex] = username[0:username.find('|')] + "|w=" + wins + "|l=" + losses + "\n"
                        #username = username[0:username.find('|')] + "|w=" + wins + "|l=" + losses + "\n"
                        #usernameFileContents.append(username)
                        #passwordFileContents.append(password + "\n")
                        
                        usernamesFile.writelines(usernameFileContents)
                        passwordsFile.writelines(passwordFileContents)

                        print(usernameFileContents)
                        usernamesFile.close() 
                        passwordsFile.close()
                        break

    elif checkWinner == 2: # They have lost!
        losses += 1
        losses = str(losses)
        wins = str(wins)

        for i in range(len(usernameFileContents)):
            userdataString = usernameFileContents[i]

            if userdataString == username:
                equalSignIndex = userdataString.find('=')
                
                # Closing the file because we're trying to overwrite it fr!
                usernamesFile.close()
                passwordsFile.close()
                
                usernamesFile = open("usernames.txt", "w") 
                passwordsFile = open("passwords.txt", "w")
                
                if userdataString == username:
                    if usernameIndex == j and username == usernameFileContents[usernameIndex] and password + "\n" == passwordFileContents[j]:
                        #passwordFileContents.pop(j)
                        #usernameFileContents.pop(i)
                        #username = username[0:username.find('|')] + "|w=" + wins + "|l=" + losses + "\n"
                        #usernameFileContents.append(username)
                        #passwordFileContents.append(password + "\n")
                        usernameFileContents[usernameIndex] = username[0:username.find('|')] + "|w=" + wins + "|l=" + losses + "\n"
                        usernamesFile.writelines(usernameFileContents)
                        passwordsFile.writelines(passwordFileContents)
                        usernamesFile.close() 
                        passwordsFile.close()
                        break

def createAccount(usernameNotFound):
    usernamesFile = open("usernames.txt", "r")
    username = input("Enter username: ") 
    usernameFileContents = usernamesFile.readlines() 

    while True: 
        if len(usernameFileContents) > 0:
            for i in range(len(usernameFileContents)):
                if username == usernameFileContents[i][0:usernameFileContents[i].find('|')]: 
                    usernameNotFound = False 
                    break
                
                elif username != usernameFileContents[i][0:usernameFileContents[i].find('|')] and i == len(usernameFileContents) - 1 and not usernameNotFound:
                    usernameNotFound = True

            if usernameNotFound:
                password = input("Enter password: ") 
                usernamesFile = open("usernames.txt", "a") 
                passwordsFile = open("passwords.txt", "a")
                
                usernamesFile.write(username + "|w=0|l=0" + "\n")
                passwordsFile.write(password + "\n")
                print("Account successfully created!") 
                usernamesFile.close()
                passwordsFile.close() 
                break
                
            else:
                print("Username already exists, please choose a different one!")
                username = input("Enter username: ") 
        else:
            password = input("Enter password: ") 
            usernamesFile = open("usernames.txt", "a") 
            passwordsFile = open("passwords.txt", "a")      
            usernamesFile.write(username + "|w=0|l=0" + "\n")
            passwordsFile.write(password + "\n")
            print("Account successfully created!") 
            usernamesFile.close()
            passwordsFile.close() 
            break
        
def displayUserData():
    usernamesFile = open("usernames.txt", "r") 
    usernameFileContents = usernamesFile.readlines()
    
    if len(usernameFileContents) > 0:
        for user in usernameFileContents:
            username = user[0:user.find('|')]
            wins = getAmountOfWins(usernameFileContents, username)
            losses = getAmountOfLosses(usernameFileContents, username)
            print("User:", username, "| Wins: ", wins, "| Losses:", losses)
            
    else:
        print("There is no user data!")


def ticTacToe(usernamesFile, passwordsFile, oldUsername, newUsername, usernameFileContents, passwordFileContents, usernameIndex, playCount):
    wins = getAmountOfWins(usernameFileContents, oldUsername)
    losses = getAmountOfLosses(usernameFileContents, oldUsername)
    drawBoard(positionalArray)

    while True:
        playerOne = input("(O) Enter a position where you'd like to go from 1-9: ")

        # Checking if input is a number
        if str(playerOne).isdigit():
            playerOne = int(playerOne)

            if 1 <= playerOne <= len(positionalArray):
                if positionalArray[playerOne - 1] == " ":
                    positionalArray[playerOne - 1] = "O"
                    drawBoard(positionalArray)

                    
                    if checkWinner(positionalArray) == 1:
                        if playCount == 0:
                            print("You won!")
                            updateUserData(usernamesFile, passwordsFile, wins, losses, newUsername, usernameFileContents, passwordFileContents, usernameIndex, 1)
                            break

                        elif playCount > 0: 
                            print("You won!")
                            for i, v in enumerate(usernameFileContents):
                                if oldUsername == v[0:v.find('|')]:
                                    usernameIndex = i
                                    newUsername = usernameFileContents[i]
                                    updateUserData(usernamesFile, passwordsFile, wins, losses, newUsername, usernameFileContents, passwordFileContents, usernameIndex, 1)
                            break 

                    if " " not in positionalArray:
                        print("It's a tie!")
                        break

                    aiMove(positionalArray)
                    drawBoard(positionalArray)

                    if checkWinner(positionalArray) == 2:  # Assuming 2 = AI wins
                        if playCount == 0:
                            print("The AI won!")
                            updateUserData(usernamesFile, passwordsFile, wins, losses, newUsername, usernameFileContents, passwordFileContents, usernameIndex, 1)
                            break

                        elif playCount > 0: 
                            print("The AI won!")
                            for i, v in enumerate(usernameFileContents):
                                if oldUsername == v[0:v.find('|')]:
                                    usernameIndex = i
                                    newUsername = usernameFileContents[i]
                                    updateUserData(usernamesFile, passwordsFile, wins, losses, newUsername, usernameFileContents, passwordFileContents, usernameIndex, 2)
                            break

                    if " " not in positionalArray:
                        print("It's a tie!")
                        break

                else:
                    print("That position is already taken!")

            else:
                print("Please enter a number between 1 and 9!")

        else:
            print("Please enter an INTEGER!")
            playerOne = input("(O) Enter a position where you'd like to go from 1-9: ")

while not quitted: #not loggedIn and not accountMade:
    if choice.isdigit():
        # Login:
        if choice == "1":
            usernamesFile = open("usernames.txt", "r") 
            passwordsFile = open("passwords.txt", "r") 

            username = input("Enter username: ") 
            password = input("Enter password: ")
            
            usernameFileContents = usernamesFile.readlines() 
            passwordFileContents = passwordsFile.readlines()
            
            wins = getAmountOfWins(usernameFileContents, username)
            losses = getAmountOfLosses(usernameFileContents, username)

            oldUsername = username
            newUsername = username + "|w=" + str(wins) + "|l=" + str(losses) + "\n"
            usernameFound = False

            if newUsername in usernameFileContents:
                for i in range(len(usernameFileContents)): 
                    if newUsername == usernameFileContents[i]:
                        usernameIndex = i
                        usernameFound = True

                    if newUsername != usernameFileContents[i] and i == len(usernameFileContents):
                        print("Username was NOT found, please try again!")
                    
                for j in range(len(passwordFileContents)):
                    if usernameIndex == j and newUsername == usernameFileContents[usernameIndex] and password + "\n" == passwordFileContents[j]:
                        print("Successfully logged in")
                        
                        loggedIn = True 
                        userChoice = input("1. Play Tic, Tac, Toe 2. Return to Menu 3. Quit: ")
                        returnedToMenu = False 

                        while not returnedToMenu: 
                            if userChoice.isdigit():
                                if userChoice == "1":
                                    ticTacToe(usernamesFile, passwordsFile, oldUsername, newUsername, usernameFileContents, passwordFileContents, usernameIndex, ticTacToeCount)                               

                                    positionalArray = [" "] * 9
                                    ticTacToeCount += 1 
                                    userChoice = input("1. Play Again, 2. Return to Menu, 3. Quit: ")                            
                                
                                elif userChoice == "2":
                                    choice = input("1. Login 2. Create an Account 3. See User Data 4. Quit (Please enter 1, 2, 3 or 4): ")
                                    returnedToMenu = True 

                                elif userChoice == "3":
                                    print("Have a nice day! :D")
                                    quitted = True 
                                    break

                                elif userChoice != "1" and userChoice != "2" and userChoice != "3":
                                    print("Please enter a valid choice!")
                                    userChoice = input("1. Play Tic, Tac, Toe 2. Return to Menu 3. Quit: ")
                            else:
                                print("Please enter an INTEGER, that is a valid choice!")
                                userChoice = input("1. Play Tic, Tac, Toe 2. Return to Menu 3. Quit: ")



                        

                    elif j == len(passwordFileContents) - 1 and not loggedIn:
                        print("Your password was wrong, please try again!")

            else: 
                print("Username was not found please try again!")

        elif choice == "2": 
            createAccount(usernameNotFound)
            choice = input("Would you like to login if so press 1 on your keyboard, if not press any other key: ")
            
            if not choice.isdigit():
                print("Have a nice day! :D") 
                break
        
        elif choice == "3":
            displayUserData()
            choice = input("1. Login 2. Create an Account 3. See User Data 4. Quit (Please enter 1, 2, 3 or 4): ")

        elif choice == "4":
            print("Have a nice day! :D")
            break

        elif choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("That is not a valid choice!")
            choice = input("1. Login 2. Create an Account 3. See User Data 4. Quit (Please enter 1, 2, 3 or 4): ")
    else: 
        print("That is not a valid choice, your choice has to be an INTEGER")
        choice = input("1. Login 2. Create an Account 3. See User Data 4. Quit (Please enter 1, 2, 3 or 4): ")
    
