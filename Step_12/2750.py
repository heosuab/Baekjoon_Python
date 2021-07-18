num = int(input())
num_list = []

for _ in range(num):
    num_list.append(int(input()))

num_list.sort()
print(*num_list, sep='\n')