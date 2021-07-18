is_sosu = [True for _ in range(0, 123456*2+1)]
is_sosu[0]==False

for i in range(0, 123456*2+1):
    if i>2:
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                is_sosu[i-1]=False
                break

while 1:
    num = int(input())

    if num==0: break
    else:
        print(is_sosu[num:num*2].count(True))