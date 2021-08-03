num, total = map(int, input().split())
coin = []
sum = 0

for _ in range(num):
    coin.append(int(input()))

for i in coin[::-1]:
    sum += total//i
    total = total%i

print(sum)