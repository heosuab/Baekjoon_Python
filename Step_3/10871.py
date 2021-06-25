length, num = map(int, input().split())
list_num = list(map(int, input().split()))

for i in range(0, length):
    if list_num[i]<num:
        print(list_num[i], end=' ')