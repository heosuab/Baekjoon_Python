
generator = [0 for _ in range(1000001)]

for i in range(1000000):
    result = sum(list(map(int, str(i))))+i
    if result<len(generator) and generator[result] == 0:
        generator[result] = i

num = int(input())
print(generator[num])
