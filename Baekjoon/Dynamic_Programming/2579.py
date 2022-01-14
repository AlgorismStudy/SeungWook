import sys

input = sys.stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]

a = [0] * 301
a[1] = [score[0], score[0]]
a[2] = [score[1], score[0]+score[1]]

for i in range(3, N+1):
    a[i] = [max(a[i-2])+score[i-1], a[i-1][0]+score[i-1]]
    
print(max(a[N]))