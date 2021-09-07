def bfs(graph, start_node):
    global bfs_visited
    queue = []

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in bfs_visited:
            bfs_visited.append(node)
            queue.extend(graph[node])

def dfs(graph, start_node):
    global dfs_visited
    dfs_visited.append(start_node)

    for node in graph[start_node]:
        if node not in dfs_visited:
            dfs(graph, node)


N, M, V = map(int, input().split())
graph = {}

for i in range(N):
    graph[i+1] = []

for _ in range(M):
    link_start, link_end = map(int, input().split())
    graph[link_start].append(link_end)
    graph[link_end].append(link_start)

for i in range(N):
    graph[i+1] = sorted(graph[i+1])

dfs_visited = []
dfs(graph, V)
print(*dfs_visited)

bfs_visited = []
bfs(graph, V)
print(*bfs_visited)






'''
# 다른 풀이(1)
N, M, V = map(int, input().split())
matrix = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

visit_list = [0]*(N+1)


def dfs(V):
    visit_list[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if(visit_list[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    queue = [V]
    visit_list[V] = 0

    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==1 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i] = 0

dfs(V)
print()
bfs(V)
'''