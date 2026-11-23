class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.mini = value
        elif value <= self.mini:  # Changed from 'if' to 'elif'
            self.stack.append(2 * value - self.mini)
            self.mini = value
        else:
            self.stack.append(value)

    def pop(self) -> None:
        if not self.stack:
            return
        if self.stack[-1] < self.mini:
            self.mini = 2 * self.mini - self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()
            
        # Optional safeguard: reset mini if stack becomes empty
        if not self.stack:
            self.mini = float('inf')

    def top(self) -> int:
        if not self.stack:
            return
        top = self.stack[-1]
        if top < self.mini:
            return self.mini
        return top

    def getMin(self) -> int:
        return self.mini
