N, M = map(int, input().split())
matrix = []
queue = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    matrix.append(list(input()))

queue = [[0, 0]]
matrix[0][0] = 1

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0<=x<N and 0<=y<M and matrix[x][y]=='1':
            queue.append([x, y])
            matrix[x][y] = matrix[a][b] + 1

print(matrix[N-1][M-1])    