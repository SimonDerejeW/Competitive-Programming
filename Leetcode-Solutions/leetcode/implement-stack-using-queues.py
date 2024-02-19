class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
        

    def push(self, x: int) -> None:
        self.que1.append(x)
        

    def pop(self) -> int:
        while len(self.que1) != 1:
            self.que2.append(self.que1.popleft())
        
        x = self.que1.popleft()
        self.que1 = self.que2
        self.que2 = deque()
        return x

        

    def top(self) -> int:
        while len(self.que1) != 1:
            self.que2.append(self.que1.popleft())
        x = self.que1.popleft()
        self.que2.append(x)
        self.que1 = self.que2
        self.que2 = deque()
        return x
        

    def empty(self) -> bool:
        if len(self.que1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()