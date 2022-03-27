import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())

visit = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            visit[j][i] = 1

def dfs(j,i):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    area = 1
    tmp = [(j,i)]
    while tmp:
        y, x = tmp.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny <0 or nx <0 or ny >= m or nx >= n):
                continue
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                area += 1
                tmp.append((ny,nx))
    return area

link = []
for i in range(n):
    for j in range(m):
        if (visit[j][i] == 0):
            visit[j][i] = 1
            link.append(dfs(j,i))

link.sort()
print(len(link))
print(*link)