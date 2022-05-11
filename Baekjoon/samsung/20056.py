import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(m)]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(k):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for fire in fireball:
        nx = (fire[0] + dx[fire[4]] * fire[3]) % n
        ny = (fire[1] + dy[fire[4]] * fire[3]) % n
        graph[nx][ny].append([nx, ny, fire[2], fire[3], fire[4]])
    fireball = []
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 1:
                fireball.append(graph[i][j][0])
            elif len(graph[i][j]) >= 2:
                flag_odd = 1
                flag_even = 1
                m_sum = 0
                v = 0
                for k in graph[i][j]:
                    if k[4] % 2 != 0:
                        flag_even = 0
                    else:
                        flag_odd = 0
                    m_sum += k[2]
                    v += k[3]
                m = m_sum // 5
                v = v // len(graph[i][j])
                if m == 0:
                    continue
                else:
                    if flag_odd or flag_even:
                        for l in range(4):
                            fireball.append([i, j, m, v, l*2])
                    else:
                        for l in range(4):
                            fireball.append([i, j, m, v, l*2+1])

count = 0
for i in fireball:
    count += i[2]

print(count)