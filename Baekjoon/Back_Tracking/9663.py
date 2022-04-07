import sys
input = sys.stdin.readline

n = int(input())
graph = [0] * n
visited = [0] * n

count = 0
def dfs(num):
    global count
    if num == n:
        count += 1
        return
    for i in range(n):
        if visited[i] == 0:
            graph[num] = i
            flag = True
            for j in range(num):
                if abs(graph[num]-graph[j]) == abs(num-j):
                    flag = False
                    break
            if flag == True:
                visited[i] = 1
                dfs(num+1)
                visited[i] = 0

dfs(0)
print(count)