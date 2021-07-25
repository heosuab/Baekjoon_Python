N, M = map(int, input().split())

selected = [False for _ in range(N+1)]
selection = []

def back_tracking(index, cnt):
    if cnt==M:
        print(*selection)
        return
    
    for i in range(index, N+1):
        if selected[i]:
            continue
        selected[i] == True
        selection.append(i)
        back_tracking(i+1, cnt+1)
        selection.pop()
        selected[i] == False

back_tracking(1, 0)