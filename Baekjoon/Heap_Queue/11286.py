import sys
input = sys.stdin.readline
import heapq

arr = []
for i in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(arr, (abs(num), num))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])