case = int(input())

for i in range(0, case):
    score_list = list(map(int, input().split()))
    mean = sum(score_list[1:])/score_list[0]
    count = 0
    for j in score_list[1:]:
        if j > mean:
            count += 1
    print("%.3f"%((count/score_list[0])*100)+"%")
    