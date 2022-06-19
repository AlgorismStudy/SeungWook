def solution(rows, columns, queries):
    graph = [[] for _ in range(rows)]
    start = 1
    for i in range(rows):
        for j in range(columns):
            graph[i].append(start)
            start += 1
    
    answer = []
    for x1, y1, x2, y2 in queries:
        up = graph[x1-1][y1-1:y2-1]
        right = [graph[i][y2-1] for i in range(x1-1, x2-1)]
        down = graph[x2-1][y1:y2]
        left = [graph[i][y1-1] for i in range(x1, x2)]

        for i, j in zip(range(y1, y2), up):
            graph[x1-1][i] = j
        for i, j in zip(range(x1, x2), right):
            graph[i][y2-1] = j
        for i, j in zip(range(y1-1, y2-1), down):
            graph[x2-1][i] = j
        for i, j in zip(range(x1-1, x2-1), left):
            graph[i][y1-1] = j
        
        answer.append(min(up+right+down+left))

    return answer

# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

rows = 100
columns = 97
queries = [[1,1,100,97]]

print(solution(rows, columns, queries))