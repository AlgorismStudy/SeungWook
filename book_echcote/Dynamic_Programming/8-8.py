import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]

d = [12345] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 12345:
    print(-1)
else:
    print(d[m])