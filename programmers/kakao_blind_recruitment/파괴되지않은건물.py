def solution(board, skill):
    graph = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            graph[r1][c1] -= degree
            graph[r2+1][c2+1] -= degree
            graph[r1][c2+1] += degree
            graph[r2+1][c1] += degree
        else:
            graph[r1][c1] += degree
            graph[r2+1][c2+1] += degree
            graph[r1][c2+1] -= degree
            graph[r2+1][c1] -= degree
    
    for i in range(len(graph)-1):
        for j in range(len(graph[0])-1):
            graph[i][j+1] += graph[i][j]
    
    for i in range(len(graph)-1):
        for j in range(len(graph[0])-1):
            graph[i+1][j] += graph[i][j]
    
    answer = 0
    for c in range(len(board)):
        for d in range(len(board[c])):
            board[c][d] += graph[c][d]
            if board[c][d] > 0:
                answer += 1
    
    return answer

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

print(solution(board, skill))