# max stack

class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = []

    def push(self,x):
        if x <= self.max[-1]:
            self.max.append(x)
        
        else:
            self.max.append(x)

    def pop(self):
        if self.stack[-1] == self.min[-1]:
            self.min.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMax(self):
        return self.max[-1]

