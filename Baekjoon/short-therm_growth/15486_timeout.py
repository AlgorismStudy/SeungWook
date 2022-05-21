import sys

input = sys.stdin.readline

n = int(input())

money = [0]*(n+1)
for day in range(n):
    t, p = map(int, input().split())
    if day + t <= n:
        money[day] += p
        for j in range(day+t, n+1):
            money[j] = max(money[day], money[j])

print(max(money))