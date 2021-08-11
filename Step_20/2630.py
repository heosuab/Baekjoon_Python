from sys import stdin

def paper(start_X, start_Y, size):
    global count_white, count_blue
    white = 0
    blue = 0
    for i in range(start_X, start_X+size):
        for j in range(start_Y, start_Y+size):
            if num_list[i][j]==1:
                blue += 1
            elif num_list[i][j]==0:
                white += 1
    if white!=0 and blue!=0:
        paper(start_X, start_Y, size//2)
        paper(start_X, start_Y+(size//2), size//2)
        paper(start_X+(size//2), start_Y, size//2)
        paper(start_X+(size//2), start_Y+(size//2), size//2)
    elif white==0:
        count_blue += 1
    elif blue==0:
        count_white += 1


num_list = []
count_white = 0
count_blue = 0

num = int(stdin.readline())

for i in range(num):
    num_list.append(list(map(int, stdin.readline().split())))

paper(0, 0, num)
print(count_white, count_blue, sep='\n')