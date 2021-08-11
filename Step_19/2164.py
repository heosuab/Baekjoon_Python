from collections import deque
from sys import stdin

card = deque(range(int(stdin.readline()), 0, -1))

while len(card)>1:
    card.pop()
    card.appendleft(card.pop())

print(*card)