import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] > A[i]:
            arr[i] = max(arr[i], arr[j]+1)

print(N - max(arr))