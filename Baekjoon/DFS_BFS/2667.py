from collections import deque

N = int(input())

zero_maps = [[0 for _ in range(N)] for _ in range(N)]
maps = [[int(_) for _ in input()] for _ in range(N)]


def bfs(cur_xy, maps, zero_maps):
    location = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque()
    queue.append(cur_xy)
    count = 0
    while queue:
        x, y = queue.popleft()
        if zero_maps[x][y] == 0:
            zero_maps[x][y] = 1
            count += 1
            for _ in location:
                next_x, next_y = x + _[0], y + _[1]
                if (
                    0 <= next_x < N
                    and 0 <= next_y < N
                    and zero_maps[next_x][next_y] == 0
                    and maps[next_x][next_y] == 1
                ):
                    next_xy = (next_x, next_y)
                    queue.append(next_xy)
    return count


count = 0
result = []
for x in range(N):
    for y in range(N):
        if zero_maps[x][y] == 0 and maps[x][y] == 1:
            count += 1
            cur_xy = (x, y)
            result.append(bfs(cur_xy, maps, zero_maps))
result.sort()

print(count)
print(*result, sep="\n")
