MAX = 100
side = [0 for _ in range(MAX+1)]

side[1], side[2], side[3], side[4], side[5] = 1, 1, 1, 2, 2

for i in range(6, MAX+1):
    side[i] = side[i-5] + side[i-1]

test = int(input())
for _ in range(test):
    num = int(input())
    print(side[num])