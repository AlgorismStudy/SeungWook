import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

players = [i for i in range(N)]
players_combi = []
for i in combinations(players, N//2) : players_combi.append(list(i))

answer = []
for t in range(len(players_combi) // 2):
    A_stats = 0
    for i in players_combi[t]:
        for j in players_combi[t]:
            A_stats += S[i][j]

    B_stats = 0
    for i in players_combi[-(t + 1)]:
        for j in players_combi[-(t + 1)]:
            B_stats += S[i][j]

    answer.append(abs(A_stats - B_stats))

print(min(answer))
