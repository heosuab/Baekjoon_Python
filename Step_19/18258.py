import sys

test = int(sys.stdin.readline())
queue = []
index = 0

for _ in range(test):
    command = list(sys.stdin.readline().split())

    if command[0]=="push":
        queue.append(int(command[1]))
    elif command[0]=="pop":
        if len(queue)<=index:
            print(-1)
        else:
            print(queue[index])
            index += 1
    elif command[0]=="size":
        print(len(queue)-index)
    elif command[0]=="empty":
        if len(queue)-index<1:
            print(1)
        else:
            print(0)
    elif command[0]=="front":
        if len(queue)-index<1:
            print(-1)
        else:
            print(queue[index])
    elif command[0]=="back":
        if len(queue)-index<1:
            print(-1)
        else:
            print(queue[-1])
