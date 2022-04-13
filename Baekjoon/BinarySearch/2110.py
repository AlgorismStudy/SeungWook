import sys

input = sys.stdin.readline

N, C = map(int, input().split())
x = sorted([int(input()) for _ in range(N)])

start, end = 0, N-1

while start <= end:
    mid = (start + end) // 2
    if mid - start + 1 < C:
        mid += 1
    else:
        mid -= 1
    