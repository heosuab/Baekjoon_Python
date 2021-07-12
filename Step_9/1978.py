num = int(input())

num_list = list(map(int, input().split()))
count = 0

for i in num_list:
    if i==1:
        count += 1
    else:
        for j in range(2, i):
            if i%j==0:
                count += 1
                break

print(num-count)