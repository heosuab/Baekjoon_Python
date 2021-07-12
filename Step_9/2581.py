start = int(input())
end = int(input())

sosu_list = []

for i in range(start, end+1):
    if i>1:
        for j in range(2, i+1):
            if j==i:
                sosu_list.append(i)
            elif i%j==0:
                break
if len(sosu_list)!=0:
    print(sum(sosu_list), min(sosu_list), sep='\n')
else:
    print(-1)