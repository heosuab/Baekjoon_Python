def dfs(X, Y):
    global matrix, count, line
    visited[X][Y] = 1
    count += 1
    
    if X>0 and matrix[X-1][Y]=='1' and visited[X-1][Y]==0:
        dfs(X-1, Y)
    if Y>0 and matrix[X][Y-1]=='1' and visited[X][Y-1]==0:
        dfs(X, Y-1)
    if X<line-1 and matrix[X+1][Y]=='1' and visited[X+1][Y]==0:
        dfs(X+1, Y)
    if Y<line-1 and matrix[X][Y+1]=='1' and visited[X][Y+1]==0:
        dfs(X, Y+1)


line = int(input())
matrix = []
visited = [[0]*line for _ in range(line)]
result = []

for _ in range(line):
    matrix.append(list(input()))

for i in range(line):
    for j in range(line):
        if matrix[i][j]=='1' and visited[i][j]==0:
            count = 0
            dfs(i, j)
            result.append(count)

result = sorted(result)
print(len(result))
print(*result, sep='\n')