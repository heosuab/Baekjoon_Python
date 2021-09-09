import sys
sys.setrecursionlimit(10**6)

def dfs(X, Y):
    global matrix, visited, w, h
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[X][Y] = 1
    for i in range(4):
        if (X+dx[i])>=0 and (X+dx[i])<=(h-1) and (Y+dy[i])>=0 and (Y+dy[i])<=(w-1):
            if matrix[X+dx[i]][Y+dy[i]]==1 and visited[X+dx[i]][Y+dy[i]]==0:
                dfs(X+dx[i], Y+dy[i])
    

case = int(input())
for _ in range(case):
    w, h, cabbage = map(int, input().split())
    matrix = [[0]*w for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    count = 0

    for _ in range(cabbage):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(h):
        for j in range(w):
            if matrix[i][j]==1 and visited[i][j]==0:
                dfs(i, j)
                count += 1

    print(count)