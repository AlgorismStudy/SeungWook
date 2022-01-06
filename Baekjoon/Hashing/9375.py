import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, kind = input().split()
        dic[kind] = dic.get(kind, 0) + 1
    ans = 1
    for k, c in dic.items():
        ans *= c + 1
    ans -= 1
    print(ans)
