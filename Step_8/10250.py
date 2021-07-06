num = int(input())

for i in range(0, num):
    H, W, N = map(int, input().split())
    print("%d%.2d"%(N%H if N%H!=0 else H, N//H+1 if N%H!=0 else N//H))