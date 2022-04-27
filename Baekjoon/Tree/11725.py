import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    first, second = map(int, input().split())
    tree[first].append(second)
    tree[second].append(first)

node = [1]
visited = [0 for _ in range(n+1)]
visited[1] = 1

result = [0 for _ in range(n+1)]
while node:
    parent = node.pop()
    for child in tree[parent]:
        if not visited[child]:
            result[child] = parent
            visited[child] = 1
            node.append(child)

print(*result[2:], sep="\n")