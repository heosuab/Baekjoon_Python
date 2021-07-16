def hanoi(num, move_from, temp, move_to):
    if num==1:
        print(move_from, move_to)
    else:
        hanoi(num-1, move_from, move_to, temp)
        print(move_from, move_to)
        hanoi(num-1, temp, move_from, move_to)    


num = int(input())
print(2**num-1)
hanoi(num, 1, 2, 3)