from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))

    return visited


def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return visited


graph = {}
N, M, V = map(int, input().split())
list = [input().split() for i in range(M)]
for i, j in list:
    if i not in graph:
        graph[i] = [j]
    elif j not in graph[i]:
        graph[i].append(j)

    if j not in graph:
        graph[j] = [i]
    elif i not in graph[j]:
        graph[j].append(i)

print(*dfs(graph, str(V)), sep=" ")
print(*bfs(graph, str(V)), sep=" ")
