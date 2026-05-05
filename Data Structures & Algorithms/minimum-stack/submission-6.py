class MinStack:

    def __init__(self):
        self.stack = []
        self.min_snapshot = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_snapshot.append(val if not self.min_snapshot else min(self.min_snapshot[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_snapshot.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_snapshot[-1]
