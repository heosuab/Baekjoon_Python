MAX = 1000001
card = [0 for _ in range(MAX+1)]

card[1], card[2] = 1, 2

num = int(input())

for i in range(3, num+1):
    card[i] = (card[i-2] + card[i-1])%15746

print(card[num])