class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize 
        self.items = []

    def isFull(self):
        return len(self.items) == self.maxSize
    
    def isEmpty(self):
        return len(self.items) == 0 
    
    def push(self, item):
        self.items.append(item) if not self.isFull() else None

    def pop(self):
        self.items.pop(len(self.items) - 1) if not self.isEmpty() else None 

    def peek(self):
        print("The item at the top of the stack is: ", self.items[len(self.items) - 1]) if not self.isEmpty() else None 

    def view(self):
        print(self.items)
    
s = Stack(5)
s.push("Ashley")
s.push("Meow")
s.push("UWU")
s.peek()
s.pop()
s.view()
