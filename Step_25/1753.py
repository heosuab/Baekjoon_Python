import heapq, sys

INF = int(1e9)

node, vertex = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

matrix = [[] for _ in range(node+1)]
distance = [INF]*(node+1)

for _ in range(vertex):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append((b, c))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in matrix[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, node+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])