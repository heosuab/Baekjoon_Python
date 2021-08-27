import sys
import heapq

test = int(sys.stdin.readline())
left = []
right = []


for _ in range(test):
    num = int(sys.stdin.readline())
    
    if len(left)<=len(right):
        heapq.heappush(left, -num)
    elif len(left)>len(right):
        heapq.heappush(right, num)

    if len(left)>0 and len(right)>0 and (-left[0])>right[0]:
        min = -heapq.heappop(left)
        max = heapq.heappop(right)
        heapq.heappush(right, min)
        heapq.heappush(left, -max)

    print(-left[0])