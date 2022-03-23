import sys

input = sys.stdin.readline

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

answer = 0
for i in range(m):
    for j in range(n):
        if j+3 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i][j+3]
            answer = max(tmp, answer)
        if i+3 < m:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
            answer = max(tmp, answer)
            
        if i+1 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
            answer = max(tmp, answer)
            
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j+1]
            answer = max(tmp, answer)
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1]
            answer = max(tmp, answer)
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j]
            answer = max(tmp, answer)
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+2][j+1]
            answer = max(tmp, answer)
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+1][j+2]
            answer = max(tmp, answer)
        if i+1 < m and j-2 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j-2]
            answer = max(tmp, answer)
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i][j+2]
            answer = max(tmp, answer)
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+2]
            answer = max(tmp, answer)

        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            answer = max(tmp, answer)
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j-1]
            answer = max(tmp, answer)
        if i-1 >= 0 and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i-1][j+1] + arr[i-1][j+2]
            answer = max(tmp, answer)
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
            answer = max(tmp, answer)

        if i-1 >= 0 and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+1]
            answer = max(tmp, answer)
        if i+1 < m and j+2 < n:
            tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
            answer = max(tmp, answer)
        if i+2 < m and j+1 < n:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j]
            answer = max(tmp, answer)
        if i+2 < m and j-1 >= 0:
            tmp = arr[i][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+2][j]
            answer = max(tmp, answer)
            
print(answer)