from collections import deque

M, N = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == 1:
            queue.append([i, j])
result = -1

location = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    result += 1
    for _ in range(len(queue)):
        cur_x, cur_y = queue.popleft()
        for _ in location:
            next_x, next_y = cur_x + _[0], cur_y + _[1]
            if 0 <= next_x < N and 0 <= next_y < M and maps[next_x][next_y] == 0:
                queue.append([next_x, next_y])
                maps[next_x][next_y] = 1

flag = True
for _ in maps:
    if 0 in _:
        flag = False
        print(-1)
        break

if flag:
    print(result)
