import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
graph = [[0]*11 for _ in range(h+1)]
result = 4

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    
def find(start, cnt):
    global result
    if cnt == min_cnt:
        if check():
            result = cnt
        return
    for i in range(start, h+1):
        for j in range(1, n):
            if not graph[i][j] + graph[i][j-1] + graph[i][j+1]:
                graph[i][j] = 1
                find(i, cnt+1)
                graph[i][j] = 0

def check():
    for i in range(1, n+1):
        tmp = i
        for j in range(1, h+1):
            if graph[j][tmp]:
                tmp += 1
            elif graph[j][tmp-1]:
                tmp -= 1
        if tmp != i:
            return False
    return True

for min_cnt in range(4):
    find(1, 0)
    if result != 4:
        print(result)
        break
else:
    print(-1)