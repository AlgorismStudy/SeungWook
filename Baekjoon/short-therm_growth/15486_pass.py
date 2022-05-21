import sys

input = sys.stdin.readline

n = int(input())

money = [0]*(n+1)
for day in range(n):
    t, p = map(int, input().split())
    if day + t <= n:
        money[day+t] = max(money[day+t], money[day] + p)
    money[day+1] = max(money[day], money[day+1])

print(money[n])