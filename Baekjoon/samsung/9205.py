import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n = int(input())
    house = list(map(int, input().split()))
    mart = [list(map(int, input().split())) for _ in range(n)]
    rock = list(map(int, input().split()))
    
    q = deque([house])
    visited = [0 for _ in range(len(mart))]
    
    result = 'sad'
    while q:
        x, y = q.popleft()
        if abs(x-rock[0]) + abs(y-rock[1]) <= 50*20:
            result = 'happy'
            break
        
        for i in range(len(mart)):
            if visited[i] or (abs(x-mart[i][0]) + abs(y-mart[i][1]) > 50*20):
                continue
            q.append(mart[i])
            visited[i] = 1
    print(result)