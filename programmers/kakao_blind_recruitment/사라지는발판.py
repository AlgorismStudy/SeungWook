def solution(board, aloc, bloc):
    global visited, graph
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    graph = [[0]*5 for _ in range(5)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            graph[i][j] = board[i][j]

    visited = [[0]*5 for _ in range(5)]
    def solve(x1, y1, x2, y2):
        global visited, graph
        if visited[x1][y1]:
            return 0
        
        flag = 0
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if nx<0 or nx>=len(board) or ny<0 or ny>=len(board[0]) or visited[nx][ny] or graph[nx][ny] == 0:
                continue
            
            visited[x1][y1] = 1
            result = solve(x2, y2, nx, ny) + 1
            visited[x1][y1] = 0
            
            if flag % 2 == 0 and result % 2 == 1:
                flag = result
            elif flag % 2 == 0 and result % 2 == 0:
                flag = max(flag, result)
            elif flag % 2 == 1 and result % 2 == 1:
                flag = min(flag, result)
        return flag
    
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1,0]
bloc = [1,2]
print(solution(board, aloc, bloc))