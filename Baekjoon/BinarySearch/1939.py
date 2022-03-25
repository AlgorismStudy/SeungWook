import sys
input = sys.stdin.readline
from collections import deque

islands, nodes = map(int, input().split())

graph = [[] for _ in range(islands+1)]
high = 1
low = 1000000000
for _ in range(nodes):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))
    high = max(high, weight)
    low = min(low, weight)

start, end = map(int, input().split())
def bfs(middle):
    queue = deque([start])
    visit = [0 for _ in range(islands+1)]
    visit[start] = 1
    while queue:
        now = queue.popleft()
        for next, weight in graph[now]:
            if not visit[next] and middle <= weight:
                queue.append(next)
                visit[next] = 1
    return visit[end]

result = low
while low <= high:
    middle = (low + high) // 2
    if bfs(middle):
        result = middle
        low = middle + 1
    else:
        high = middle - 1

print(result)