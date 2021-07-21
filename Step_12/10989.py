import sys

num = int(sys.stdin.readline())
num_list = [0 for _ in range(10001)]

for _ in range(num):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(num_list[i]):
        print(i)