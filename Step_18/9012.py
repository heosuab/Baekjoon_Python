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

    def top(self):
        if len(self.stack) >= 1:
            return self.stack[-1]
        return -1

test = int(sys.stdin.readline())

for _ in range(test):
    stack = Stack()
    brackets = list(sys.stdin.readline())
    for i in brackets:
        if i==')' and stack.top()=='(':
            stack.pop()
            continue
        stack.push(i)
        if i=='\n':
            break
    if stack.size()-1==0:
        print('YES')
    else:
        print('NO')