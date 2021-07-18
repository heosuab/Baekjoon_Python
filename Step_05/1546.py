num = int(input())
score_list = list(map(float, input().split()))
max = max(score_list)

for i in range(0, num):
    score_list[i] = (score_list[i]/max)*100

print(sum(score_list)/len(score_list))