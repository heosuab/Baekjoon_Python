num = int(input())

for i in range(num):
    if i==0:
        min_price = list(map(int, input().split()))
        continue
    first, second, third = map(int, input().split())
    first += min(min_price[1], min_price[2])
    second += min(min_price[0], min_price[2])
    third += min(min_price[0], min_price[1])

    min_price = [first, second, third]

print(min(min_price))