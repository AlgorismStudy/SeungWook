import sys

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]

zero = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append((i,j))

def dfs(cnt):
    if cnt == len(zero):
        [print(*a, sep=' ') for a in graph]
        sys.exit()
    x, y = zero[cnt]
    for i in search(x, y):
        graph[x][y] = i
        dfs(cnt + 1)
        graph[x][y] = 0

def search(x, y):
    num = set(range(1, 10))
    for i in range(9):
        if graph[x][i] in num:
            num.remove(graph[x][i])
        if graph[i][y] in num:
            num.remove(graph[i][y])
    x //= 3
    y //= 3
    for i in range(x * 3, (x + 1) * 3):
        for j in range(y * 3, (y + 1) * 3):
            if graph[i][j] in num:
                num.remove(graph[i][j])
    return num

dfs(0)