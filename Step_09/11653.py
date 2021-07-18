num = int(input())
insu = 2

while num!=1:
    if num%insu==0:
        print(insu)
        num = num//insu
    else:
        insu+=1