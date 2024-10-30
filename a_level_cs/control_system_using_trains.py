# a lil control system for my year 12 computer science homework our task was to make:
'''
Write a Python program that simulates a control system for London Underground station using queues and stacks. 

Your program should introduce the idea of trains waiting at a junction before entering the station platform. 

The junction connects four separate lines to one platform, all heading in the same direction.

Only one train is allowed to be on the platform at any given time.

Some trains might be late so to reduce the fine the company should pay, they should obviously arrive on the platform first BUT there might be a train in front of them.
'''
import time 
class Train: 
    def __init__(self, line, late=False):
        self.line = line 
        self.late = late

class JunctionQueue: 
    def __init__(self, junctionSize): 
        self.trainsInJunction = [] 
        self.junctionSize = junctionSize 

    def isJunctionFull(self): 
        return len(self.trainsInJunction) >= self.junctionSize

    def isJunctionEmpty(self): 
        return len(self.trainsInJunction) == 0 

    def enqueue(self, train):
        self.trainsInJunction.append(train) if not self.isJunctionFull() else print("The junction is full, cannot add train!") 

    def dequeue(self): 
        return self.trainsInJunction.pop(0) if not self.isJunctionEmpty() else None 

    def viewJunction(self):
        for i, v in enumerate(self.trainsInJunction):
            print(f"Train Queue Position: {str(i)}, Line: {v.line}, Train Late: {v.late}")

    def sortJunction(self): 
        sorted = False 
        while not sorted:
            sorted = True
            for i in range(len(self.trainsInJunction) - 1):
                currentTrain = self.trainsInJunction[i]
                nextTrain = self.trainsInJunction[i + 1]
                
                if not currentTrain.late and nextTrain.late:
                    self.trainsInJunction[i], self.trainsInJunction[i + 1] = nextTrain, currentTrain
                    sorted = False  

class PlatformStack: 
    def __init__(self): 
        self.trainsOnPlatform = [] 
        self.platformSize = 1 

    def isPlatformFull(self):
        return len(self.trainsOnPlatform) == self.platformSize
    
    def isPlatformEmpty(self):
        return len(self.trainsOnPlatform) == 0 
    
    def push(self, train): 
        self.trainsOnPlatform.append(train) if not self.isPlatformFull() else print("Platform is full, cannot push train onto the platform!") 
    
    def pop(self):
        self.trainsOnPlatform.pop(len(self.trainsOnPlatform) - 1) if not self.isPlatformEmpty() else None  

    def viewPlatform(self): 
        for train in self.trainsOnPlatform: 
            print(f"Line: {train.line}, Train Late: {train.late}")
        
junction = JunctionQueue(4)
platform = PlatformStack()

def loadingScreenKindOfLmao():
    print("Loading Passengers Onto Train.", end="\r")
    time.sleep(1)
    print("Loading Passengers Onto Train..", end="\r")
    time.sleep(1)
    print("Loading Passengers Onto Train...", end="\r")
    time.sleep(1)

    print("Train Beginning To Leave Platform.", end="\r")
    time.sleep(1)
    print("Train Beginning To Leave Platform..", end="\r")
    time.sleep(1)
    print("Train Beginning To Leave Platform...", end="\r")
    time.sleep(1)

def createTrains(): 
    if not junction.isJunctionFull():
        trainsToBeMade = input("How many trains would you like to make (Enter an integer): ") 
        trainsMade = False 

        while not trainsMade: 
            if trainsToBeMade.isdigit(): 
                if int(trainsToBeMade) <= junction.junctionSize:
                    for i in range(1, int(trainsToBeMade) + 1):
                        trainLine = input(f"What is the name of the train line {str(i)}: ") 
                        late = input("1. Train was late, 2. Train not late (Enter 1 or 2): ") 

                        if late.isdigit(): 
                            if late == "1":
                                train = Train(trainLine, late=True) 
                                junction.enqueue(train)

                            elif late == "2": 
                                train = Train(trainLine, late=False)
                                junction.enqueue(train)

                            elif late != "1" and late != "2":
                                print("Please enter a valid choice!") 
                                late = input("1. Train was late, 2. Train not late (Enter 1 or 2): ")   
                        else: 
                            print("Please enter a valid choice!") 
                            late = input("1. Train was late, 2. Train not late (Enter 1 or 2): ") 

                    trainsMade = True
                else:
                    print("The amount of trains you make has to be less than your junction size!")
                    trainsToBeMade = input("How many trains would you like to make (Enter an integer): ") 

            else: 
                print("Please enter a valid amount of trains you want to make!")
                trainsToBeMade = input("How many trains would you like to make (Enter an integer): ") 
    else:
        print("Cannot add train to junction, due to it being full!")

while True: 
    choice = input("1. Create Train And Add to Junction, 2. Push Train onto the Platform: ") 

    if choice.isdigit():
        if choice == "1":
            createTrains()
            junction.sortJunction()
            junction.viewJunction()

        elif choice == "2":
            if not junction.isJunctionEmpty():
                platform.push(junction.trainsInJunction[0])
                junction.dequeue() 
                platform.viewPlatform()
                time.sleep(1)
                loadingScreenKindOfLmao()
                platform.pop()

            else:
                print("There are no trains in the junction to push onto the platform!") 

        elif choice != "1" and choice != "2": 
            print("Please enter a valid choice!")
            continue

    else: 
        print("Please enter a valid choice!")
        continue 
