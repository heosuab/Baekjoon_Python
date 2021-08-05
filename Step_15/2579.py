max_value = [[0, 0], [0, 0]]
stair_num = int(input())

for i in range(stair_num):
    value = int(input())
    if i==0:
        max_value[0] = [value, value]
    elif i==1:
        max_value[1] = [max_value[0][0]+value, value]
    else:
        if i%2==0:
            max_value[0] = [max_value[1][1]+value, max(max_value[0][0]+value, max_value[0][1]+value)]
        else:
            max_value[1] = [max_value[0][1]+value, max(max_value[1][0]+value, max_value[1][1]+value)]

print(max(max_value[(stair_num-1)%2]))