A, B, V = map(int, input().split())

start, i, day = A, 1, A-B

x = (V-A)/day

print(int(x)+1 if x==int(x) else int(x)+2)