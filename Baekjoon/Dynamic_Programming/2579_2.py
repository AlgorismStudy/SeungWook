import sys

input = sys.stdin.readline

N = int(input())

a = [0] * 301
for i in range(N):
    a[i] = int(input())
    
score = [0] * 301
score[0] = a[0]
score[1] = a[0] + a[1]
score[2] = max(a[1] + a[2], a[0] + a[2])

for i in range(3, N):
    score[i] = max(score[i - 3] + a[i - 1] + a[i], score[i - 2] + a[i])
    
print(score[N - 1])