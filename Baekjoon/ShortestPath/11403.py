import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] != 0 or graph[a][k]+graph[k][b] == 2:
                graph[a][b] = 1

for a in graph:
    print(*a, sep=" ")