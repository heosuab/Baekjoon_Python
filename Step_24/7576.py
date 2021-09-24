import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
matrix = []
queue = deque()
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if matrix[i][j]==1:
            queue.append([i, j])

while queue:
    a, b = queue.popleft()

    for i in range(4):
        x = a+dx[i]
        y = b+dy[i]
        if 0<=x<N and 0<=y<M and matrix[x][y]==0:
            matrix[x][y] = matrix[a][b]+1
            queue.append([x, y])

for i in range(N):
    if 0 in matrix[i]:
        result = 0
        break
    if max(matrix[i])>result:
        result = max(matrix[i])

print(result-1)