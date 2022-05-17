import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for i in range(n*n)]

visited = [0 for i in range(n*n)]
dist = [(-1,0), (0,1), (1,0), (0,-1)]

