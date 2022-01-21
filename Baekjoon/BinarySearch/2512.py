import sys

input = sys.stdin.readline

N = int(input())
request = list(map(int, input().split()))
M = int(input())

start, end = 1, max(request)

while end >= start:
    mid = (start + end) // 2
    result = 0
    for i in request:
        if mid < i:
            result += mid
        else:
            result += i
    if result > M:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)