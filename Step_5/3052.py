count = []

for i in range(0, 10):
    count.append(int(input())%42)

count = set(count)
print(len(count))