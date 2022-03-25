import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1-1].append(node2-1)
    graph[node2-1].append(node1-1)
    
def dfs(i):
    if visit[i] > 0:
        return
    
    visit[i] = 1
    for j in graph[i]:
        dfs(j)

visit = [0 for _ in range(n)]
link = 0
for i in range(n):
    if visit[i] == 0:
        link += 1
        dfs(i)

print(link)