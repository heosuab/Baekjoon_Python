def right(least, middle, max):
    if least**2 + middle**2 == max**2:
        return "right"
    else:
        return "wrong"

while 1:
    num_list = list(map(int, input().split()))
    num_list.sort()
    
    if num_list.count(0)==3:
        break
    print(right(*num_list))

    