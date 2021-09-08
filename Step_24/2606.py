def bfs(start_node):
    global com, link

    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        for i in range(1, com+1):
            if (i not in visited) and (link[node][i]==1):
                visited.append(i)
                queue.append(i)

    return len(visited)

com = int(input())
link = [[0]*(com+1) for _ in range(com+1)]

num_link = int(input())
for _ in range(num_link):
    start, end = map(int, input().split())
    link[start][end] = 1
    link[end][start] = 1

print(bfs(1)-1)