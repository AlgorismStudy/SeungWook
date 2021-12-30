import sys

N = []
for i in range(int(input())):
    N.append(list(map(int, sys.stdin.readline().split())))

N = sorted(N, key=lambda x: x[0])
N = sorted(N, key=lambda x: x[1])

final = 0
conut = 0
for i, j in N:
    if i >= final:
        final = j
        conut += 1

print(conut)
