import sys

input = sys.stdin.readline

N = int(input())

arr = [0]
for i in range(1, N+1):
  t, p = map(int, input().split())
  arr.append((i, t, p))

money = [0]*(N+1)
for i in range(1, N+1):
  day, t, p = arr[i]
  if day + t <= N+1:
    money[i] += p
    for j in range(day+t, N+1):
      money[j] = max(money[day], money[j])
 
print(max(money))