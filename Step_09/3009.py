coord_X, coord_Y = [], []

for i in range(0, 3):
    X, Y = map(int, input().split())
    coord_X.append(X)
    coord_Y.append(Y)

print(max(coord_X) if coord_X.count(max(coord_X))==1 else min(coord_X), max(coord_Y) if coord_Y.count(max(coord_Y))==1 else min(coord_Y)) 