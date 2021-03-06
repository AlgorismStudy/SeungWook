import sys

input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
n, m = map(int, input().split()) # 노드의 개수, 간선의 개수를 입력받기
start = int(input()) # 시작 노드 번호를 입력받기

graph = [[] for _ in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (n+1) # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m): # 모든 간선 정보를 입력받기
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def get_smallest_node(): # 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해서 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1): # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
        now = get_smallest_node() # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        visited[now] = True
        for j in graph[now]: # 현재 노드와 연결된 다른 노드를 확인
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1): # 모든 노드로 가기 위한 최단 거리를 출력
    if distance[i] == INF: # 도달할 수 없는 경우, 무한출력
        print("INFINITY")
    else: # 도달할 수 있는 경우 거리를 출력
        print(distance[i])