class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValStack = []

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.minStack.append(val)
            self.minValStack.append(val)
        else:
            if val<self.minValStack[-1]:
                self.minValStack.append(val)
            else:
                self.minValStack.append(self.minValStack[-1])
            self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.minValStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minValStack[-1]
        
        
