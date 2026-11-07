class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if self.stack:
            current_min = min(value, self.stack[-1][1])
        else:
            current_min = value

        self.stack.append((value, current_min))

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")

        value, _ = self.stack.pop()
        return value

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")

        return self.stack[-1][0]

    def get_min(self) -> int:
        if not self.stack:
            raise IndexError("get_min from empty stack")

        return self.stack[-1][1]


stack = Stack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min() == -3)
stack.pop()
print(stack.top() == 0)
print(stack.get_min() == -2)
