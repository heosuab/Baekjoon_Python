start, end = map(int, input().split())

for i in range(start, end+1):
    if i>2:
        is_sosu = True
        for j in range(2, int(i**0.5)+2):
            if i%j==0:
                is_sosu = False
                break
        if is_sosu:
            print(i)
    elif i==2:
        print(2)
