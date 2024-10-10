# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = deque()
        self.maxSize = maxSize
        self.count = 0
        

    def push(self, x: int) -> None:
        if self.count < self.maxSize:
            self.stack.append(x)
            self.count += 1
        

    def pop(self) -> int:
        if self.count > 0:
            self.count -= 1
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k,len(self.stack))
        curr = []
        for i in range(k):
            node = self.stack.popleft()
            node += val
            curr.append(node)
        curr = curr[::-1]
        for i in range(len(curr)):
            self.stack.appendleft(curr[i])
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)