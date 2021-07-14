##시간초과/업뎃 예정

start, end = map(int, input().split())
is_sosu = [True for i in range(start, end+1)]

for i in range(start, end+1):
    if is_sosu[i-start]:
        print("now", i)
        for j in range(2, int(i**0.5)+2):
            if j==int(i**0.5)+1:
                print(i)
                for k in range(i*2, end, i):
                    is_sosu[k-start]=False
                    print(is_sosu)
            elif i%j==0:
                is_sosu[i-start]=False
                break
