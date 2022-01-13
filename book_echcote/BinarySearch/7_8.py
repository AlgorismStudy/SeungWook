import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

height = list(map(int, input().split()))

start = 0
end = max(height)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for hei in height:
        if hei > mid:
            total += hei - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)