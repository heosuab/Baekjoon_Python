import sys

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) >= 1:
            data = self.stack.pop()
            return data
        return -1

    def stackSum(self):
        return sum(self.stack)


line = int(sys.stdin.readline())
stack = Stack()

for _ in range(line):
    data = int(sys.stdin.readline())
    if data != 0:
        stack.push(data)
    else:
        stack.pop()

print(stack.stackSum())