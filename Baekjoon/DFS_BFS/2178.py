from collections import deque

N, M = map(int, input().split())

location = [(1, 0), (0, 1), (-1, 0), (0, -1)]

empty_list = []
maps = []
for _ in range(N):
    empty_list.append([0 for _ in range(M)])
    maps.append(list(map(int, list(input()))))

queue = deque()
queue.append((0, 0))
empty_list[0][0] = 1
while queue:
    cur_y, cur_x = queue.popleft()
    maps[cur_y][cur_x] = 0
    for i in range(4):
        next_y, next_x = cur_y + location[i][0], cur_x + location[i][1]
        if (
            0 <= next_y < len(maps)
            and 0 <= next_x < len(maps[0])
            and maps[next_y][next_x] == 1
        ):
            queue.append((next_y, next_x))
            empty_list[next_y][next_x] = empty_list[cur_y][cur_x] + 1
            maps[next_y][next_x] = 0

print(empty_list[N - 1][M - 1])
