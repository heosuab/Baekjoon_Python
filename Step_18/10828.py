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

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) >= 1:
            return 0
        return 1

    def top(self):
        if len(self.stack) >= 1:
            return self.stack[-1]
        return -1


test = int(sys.stdin.readline())
new_stack = Stack()

for _ in range(test):
    command = list(sys.stdin.readline().split())
    if command[0]=="push":
        new_stack.push(int(command[1]))
    elif command[0]=="pop":
        print(new_stack.pop())
    elif command[0]=="size":
        print(new_stack.size())
    elif command[0]=="empty":
        print(new_stack.empty())
    elif command[0]=="top":
        print(new_stack.top())