import sys
input = sys.stdin.readline
from collections import deque

a,b,c = map(int, input().split())

q = deque()
visited = [[0]*(b+1) for _ in range(a+1)]

def move(c, d):
    if not visited[c][d]:
        visited[c][d] = 1
        q.append((c,d))

result = []
def bfs():
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        z = c - x - y
        if x == 0:
            result.append(z)
        
        if x>0 and y<b:
            water = min(x, b-y)
            move(x-water, y+water)
        
        if x>0 and z<c:
            water = min(x, c-z)
            move(x-water, y)
        
        if y>0 and x<a:
            water = min(y, a-x)
            move(x+water, y-water)
        
        if y>0 and z<c:
            water = min(y, c-z)
            move(x, y-water)
        
        if z>0 and x<a:
            water = min(z, a-x)
            move(x+water, y)
        
        if z>0 and y<b:
            water = min(z, b-y)
            move(x, y+water)
        
bfs()
result.sort()
print(*result)