import sys
input = sys.stdin.readline

V, E = map(int, input().split())

arr = []
for _ in range(E):
    A, B, C = map(int, input().split())
    arr.append((C, A, B))

parent = [i for i in range(V+1)]
    
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
arr.sort()
result = 0
for ar in arr:
    cost, a, b = ar
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)    