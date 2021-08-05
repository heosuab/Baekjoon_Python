line = int(input())

for i in range(line):
    input_list = list(map(int, input().split()))
    if i==0:
        num_list = input_list
        continue
    for j in range(i+1):
        if j==0:
            input_list[j] += num_list[j]
        elif j==i:
            input_list[j] += num_list[j-1]
        else:
            input_list[j] += max(num_list[j-1], num_list[j])
    num_list = input_list

print(max(num_list))