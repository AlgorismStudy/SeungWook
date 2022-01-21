import sys

input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m): # A와 B가 서로에게 가는 비용은 1이라고 가정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split()) # 거쳐 갈 노드 k와 최종 목적지 노드 x를 입력받기

for a in range(1, n+1): # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n+1): # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x] # 수행된 결과를 출력

if distance >= INF:
    print("-1")
else:
    print(distance)