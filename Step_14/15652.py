N, M = map(int, input().split())

selection = []

def back_tracking(index, cnt):
    if cnt==M:
        print(*selection)
        return
    
    for i in range(index, N+1):
        selection.append(i)
        back_tracking(i, cnt+1)
        selection.pop()

back_tracking(1, 0)