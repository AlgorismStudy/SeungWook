import sys
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    graph.append((x, y, z, i))

def mindis(i, j):
    return min(abs(i[0]-j[0]), abs(i[1]-j[1]), abs(i[2]-j[2]))

dis = []
for i in range(3):
    regraph = sorted(graph, key=lambda x:x[i])
    for j in range(n-1):
        dis.append((mindis(regraph[j], regraph[j+1]), regraph[j][3], regraph[j+1][3]))
dis.sort()

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
count = 0
parent = [i for i in range(n+1)]
for d, start, end in dis:
    if find(start) != find(end):
        union(start, end)
        result += d
        count += 1
        if count == n - 1:
            break

print(result)