import sys

list_num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

target_num = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

for i in range(target_num):
    if target[i] in num_list:
        print("1")
    else:
        print("0")