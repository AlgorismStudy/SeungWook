import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

INF = int(1e9)
distance = [INF] * (n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY") 
    else:
        print(distance[i])               