import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(M):
    A, B, C = map(int, input().split())
    arr.append((C, A, B))
arr.sort()

parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
last = 0
for cost, a, b in arr:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        last = cost

print(result - last)