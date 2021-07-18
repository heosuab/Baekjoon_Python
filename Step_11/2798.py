N, M = map(int, input().split())
num = list(map(int, input().split()))

sum = []

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum.append(num[i]+num[j]+num[k])
sum.sort()

for index, value in enumerate(sum):
    if index>0 and value > M:
        print(sum[index-1])
        break
    if index==len(sum)-1:
        print(max(sum))