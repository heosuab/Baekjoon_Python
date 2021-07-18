num = int(input())

for i in range(0, num):
    score_list = list(input())
    count = 0
    score = 0
    for j in range(0, len(score_list)):
        if(score_list[j]=='O'):
            count += 1
            score += count
        else:
            count = 0
    print(score)