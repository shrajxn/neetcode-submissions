class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]
    def getMin(self) -> int:
        curr=float("inf")
        for val in self.stack:
            curr=min(curr,val)
        return curr
            
