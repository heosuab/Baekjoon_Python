N, M = map(int, input().split())

selection = []

def back_tracking(cnt):
    if cnt==M:
        print(*selection)
        return
    for i in range(1, N+1):
        selection.append(i)
        back_tracking(cnt+1)
        selection.pop()

back_tracking(0)