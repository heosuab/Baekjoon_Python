import heapq
import sys

test = int(sys.stdin.readline())
min_heap = []

for _ in range(test):
    num = int(sys.stdin.readline())
    if num==0:
        print(heapq.heappop(min_heap)[1] if len(min_heap)>0 else "0")
    else:
        heapq.heappush(min_heap, (abs(num), num))