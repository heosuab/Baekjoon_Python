def quard_Tree(start_X, start_Y, size):
    same = True
    number = image[start_X][start_Y]
    for i in range(size):
        for j in range(size):
            if image[start_X+i][start_Y+j]!=number:
                same = False
                break
    if same:
        print(number, end='')
    else:
        print("(", end='')
        new_size = size//2
        quard_Tree(start_X, start_Y, new_size)
        quard_Tree(start_X, start_Y+new_size, new_size)
        quard_Tree(start_X+new_size, start_Y, new_size)
        quard_Tree(start_X+new_size, start_Y+new_size, new_size)
        print(")", end='')


num = int(input())
image = [list(map(int, input())) for _ in range(num)]

quard_Tree(0, 0, num)