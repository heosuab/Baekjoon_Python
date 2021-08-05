multiple = 1
num = int(input())

factor = list(map(int, input().split()))
print(min(factor)*max(factor))