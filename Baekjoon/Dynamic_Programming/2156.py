import sys
input = sys.stdin.readline

n = int(input())
grapes = [int(input()) for _ in range(n)]

if n == 1:
    max_g = [grapes[0]]
elif n == 2:
    max_g = [grapes[0], grapes[0]+grapes[1]]
else:
    max_g = [grapes[0], grapes[0]+grapes[1]]
    max_g.append(max(grapes[0]+grapes[1], grapes[0]+grapes[2], grapes[1]+grapes[2]))

    for i in range(3, n):
        max_g.append(max(max_g[i-1], max_g[i-2]+grapes[i], max_g[i-3]+grapes[i-1]+grapes[i]))

print(max_g[n-1])