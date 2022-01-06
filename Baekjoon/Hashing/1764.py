import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = {input().strip(): 1 for i in range(N)}

result = []
for _ in range(M):
    s = input().strip()
    if s in dic:
        result.append(s)

result.sort()

print(len(result))
for _ in result:
    print(_)
