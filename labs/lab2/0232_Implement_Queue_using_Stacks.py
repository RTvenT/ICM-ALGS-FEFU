class MyQueue:
    def __init__(self):
        self.forward = []
        self.backward = []


    def push(self, x: int) -> None:
        self.forward.append(x)


    def pop(self) -> int:
        while self.forward:
            self.backward.append(self.forward.pop())
            
        top = self.backward.pop()
        
        while self.backward:
            self.forward.append(self.backward.pop())
            
        return top


    def peek(self) -> int:
        while self.forward:
            self.backward.append(self.forward.pop())
            
        top = self.backward[-1]
        
        while self.backward:
            self.forward.append(self.backward.pop())
            
        return top
    
    
    def empty(self) -> bool:
        return not self.forward
