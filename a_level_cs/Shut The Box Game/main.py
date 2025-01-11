'''
made this game to help learn tkinter and to improve my overall understanding of python 
by asxhes
'''
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import random 
from tkinter import messagebox # ts shit is so dumb why do i have to import messagebox from tkinter even though i imported everything??
import threading

root = Tk()
picturesFolder = Path("Pictures")

root.title("STBG") 
root.geometry("555x500") 
root.resizable(False, False) # prevents the ui from being resized on height and width
root.iconbitmap("dice.ico")

images = {}
btns = {}
labels = {}
sum = []
currentChoices = [] 

gameLost = False  
gameWon = False

for i,file in enumerate(picturesFolder.iterdir()):
    # file.stem gets the name of the file without the extension
    if file.stem.isdigit():
        images[f"img{file.stem}"] = Image.open(file) # loading thwe image file
        images[f"img{file.stem}"] = images[f"img{file.stem}"].resize((50, 75)) # resizing the loaded image
        images[f"imgTk{file.stem}"] = ImageTk.PhotoImage(images[f"img{file.stem}"]) # converting the image extension to a format tkinter can read cuz its dumb asf
    else: 
        images["background"] = Image.open(file)
        images["background"] = images["background"].resize((555, 500))
        images["backgroundTk"] = ImageTk.PhotoImage(images["background"])      

bgLabel = Label(root, image=images["backgroundTk"])
bgLabel.place(relwidth=1, relheight=1)
# relwidth and relheight specify the width and height the label should take relative to its parent container (which is root in this case)
# the numbers are 1 meaning they should take up 100% of the width and height of the parent container so it should take up all the space 
# this makes it act as the background

def checkWL(dice):
    currentChoices.clear()
    for item in btns:
        if btns[item].cget("state") != DISABLED: 
            num = int(item[3:])
            currentChoices.append(num) 

    if len(currentChoices) == 1:
        if currentChoices[0] != dice:
            return "You lost!" # this means they lost

        else:
            return "You won!"
    else: 
        for i in range(len(currentChoices)): # outer loop to get the current number we're trying to check    
            if currentChoices[i] == dice:
                return "Passed"
              
            for j in range(i + 1, len(currentChoices)): # inner loop checks every number after the current number (i+1) in the list and sees if it can equal dice
                if currentChoices[i] + currentChoices[j] == dice:
                    return "Passed"
                
        return "You lost!"
                

def onClick(num):
    #global sum
    sum.append(num) 

def reset():
    #global sum, resetFlag 
    global resetFlag
    resetFlag = True
    sum.clear()

def gameLogic(): 
    global clicked, gameLost, gameWon, resetFlag, oldDice, dice
    clicked = False 
    gameLost = False 
    gameWon = False 
    resetFlag = False 
    oldDice = False 

    while not gameLost and not gameWon: 
        if resetFlag:
            resetFlag = False
            clicked = False
            oldDice = True
            messagebox.showinfo("STBG", "Successfully reset chosen options!")
        if not clicked:
            if not oldDice:
                dice = random.randint(2, 12)
            
            labels["rollValue"].config(text=f"The number you rolled is {dice}")

            clicked = True 
            oldDice = False 

            if checkWL(dice) == "You lost!":
                messagebox.showerror("STBG", "No valid moves left, game over!")
                answer = messagebox.askquestion("STBG", "Do you want to play again?")
                if answer == "yes":
                    clicked = False 
                    gameLost = False 
                    gameWon = False 
                    resetFlag = False 
                    oldDice = False 
                    sum.clear()
                    for item in btns:
                        btns[item].config(state=NORMAL)

                    continue
                else:
                    gameLost = True
                    root.destroy()

            while len(sum) == 0:
                pass 

            if len(sum) == 1:
                if sum[0] == dice:
                    btns[f"btn{str(sum[0])}"].config(state=DISABLED)
                    clicked = False
                    sum.clear()
                    continue  
                else:
                    while True:
                        if len(sum) > 1:
                            break

            
            if len(sum) > 1:
                for i in range(len(sum)): # outer loop to get the current number we're trying to check    
                    for j in range(i + 1, len(sum)): # inner loop checks every number after the current number (i+1) in the list and sees if it can equal dice
                        if sum[i] == sum[j]:
                            messagebox.showerror("STBG", "You cannot choose the same numbers twice!")
                            clicked = False
                            oldDice = True
                            sum.clear()
                
                for i, v in enumerate(sum):
                    if i < len(sum) - 1:
                        if len(sum) == 2 and v + sum[i + 1] == dice:
                            dice = random.randint(2, 12)
                            btns[f"btn{str(sum[i])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 1])}"].config(state=DISABLED)
                            clicked = False
                            sum.clear()
                            break 

                        while len(sum) == 2:
                            pass

                        if len(sum) == 3 and v + sum[i + 1] + sum[i + 2] == dice:
                            dice = random.randint(2, 12)
                            btns[f"btn{str(sum[i])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 1])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 2])}"].config(state=DISABLED)
                            clicked = False
                            sum.clear()
                            break 

                        while len(sum) == 3:
                            pass

                        if len(sum) == 4 and v + sum[i + 1] + sum[i + 2] + sum[i + 3] == dice:
                            dice = random.randint(2, 12)
                            btns[f"btn{str(sum[i])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 1])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 2])}"].config(state=DISABLED)
                            btns[f"btn{str(sum[i + 3])}"].config(state=DISABLED)
                            clicked = False
                            sum.clear()
                            break 

                continue

        
        
for i2 in range(1, 11):
    btns[f"btn{i2}"] = Button(root, text=str(i2), image=images[f"imgTk{str(i2)}"], width=50, height=75, command=lambda i2=i2: onClick(i2))
    # i2=i2 means that buttons get their value of i2 at the time the button is created 
    # this prevents all the buttons from having the same value because of the for loop ending at 10 so if i didnt have that 
    btns[f"btn{i2}"].grid(row=0, column = i2 - 1, sticky="s") # "stciky" allows us to have more control on the positioning e.g in this case
# sticky = "s" means the btns shld be positioned "sOUTH" meaning the bottom its dumb asf ikr 
resetBtn = Button(root, text="Reset Choices", command=reset, width=70)
resetBtn.grid(row=1, column=0, columnspan=10, sticky="ew") # column span ensures that the button
root.grid_rowconfigure(0, weight=1) # first arg is the row index we're configuring (0 is the 1st row), 2nd arg is the weight essentially how much space should the row
# take relative to all the other rows (watch that coding guy's video again u shld remember that all rows are like relative to eachother
# if weight is set to any positive number like 1 it will take up all the space this is why our buttons go to the bottom
labels["diceRoll"] = Label(root, image=images["backgroundTk"])
labels["rollValue"] = Label(root, font=("Arial", 16, "bold"))
labels["rollValue"].grid(row=0, columnspan=10)
thread = threading.Thread(target=gameLogic) # multithreading so i can run the main loop AND this game logic thread type shi
thread.daemon = True # ensures the thread stops when the main program exits
thread.start() # like coroutine.resume in lua we're starting the thread
root.mainloop()
    

