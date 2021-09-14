import sys

test = int(sys.stdin.readline())
for _ in range(test):
    num = int(sys.stdin.readline())
    matrix = [[0]*(num+1) for _ in range(num+1)]
    file_size = list(map(int, sys.stdin.readline().split()))
    sum_size = []

    for i in range(num):
        sum_size.append(sum(file_size[:i+1]))

    for i in range(1, num):
        for j in range(1, num-i+1):
            case = []
            if i==1:
                matrix[j][j+i] = file_size[j-1] + file_size[j]
                continue
            for k in range(j, j+i):
                if j-2<0:
                    case.append(matrix[j][k] + matrix[k+1][j+i] + sum_size[j+i-1])
                else:
                    case.append(matrix[j][k] + matrix[k+1][j+i] + sum_size[j+i-1] - sum_size[j-2])
            matrix[j][j+i] = min(case)
    
    print(matrix[1][num])