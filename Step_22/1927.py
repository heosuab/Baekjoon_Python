import heapq
import sys

test = int(sys.stdin.readline())
max_heap = []

for _ in range(test):
    num = int(sys.stdin.readline())
    if num==0:
        print(heapq.heappop(max_heap) if len(max_heap)>0 else "0")
    else:
        heapq.heappush(max_heap, num)