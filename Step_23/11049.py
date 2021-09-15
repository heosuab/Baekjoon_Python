num = int(input())

matrix = [[0]*(num) for _ in range(num)]
matrix_size = []

for _ in range(num):
    matrix_size.append(list(map(int, input().split())))

for i in range(1, num):
    for j in range(num-i):
        if i==1:
            matrix[j][j+i] = matrix_size[j][0]*matrix_size[j][1]*matrix_size[j+i][1]
        else:
            case = []
            for k in range(i):
                case.append(matrix[j][j+k] + matrix[j+k+1][j+i] + matrix_size[j][0]*matrix_size[j+k][1]*matrix_size[j+i][1])
            matrix[j][j+i] = min(case)

print(matrix[0][num-1])
