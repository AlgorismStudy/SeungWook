import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*n for _ in range(n)]

for i in range(int(input())):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

