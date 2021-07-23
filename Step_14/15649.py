N, M = map(int, input().split())

selected = [False for _ in range(N+1)]
selection = []

def dfs(cnt):
    if(cnt == M):
        print(*selection)
        return
    
    for i in range(1, N+1):
        if(selected[i]):
            continue
        selected[i] = True
        selection.append(i)
        dfs(cnt + 1)
        selection.pop()
        selected[i] = False
        
dfs(0)