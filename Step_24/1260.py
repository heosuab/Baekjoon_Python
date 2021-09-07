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

dfs_visited = []
dfs(graph, V)
print(*dfs_visited)

bfs_visited = []
bfs(graph, V)
print(*bfs_visited)