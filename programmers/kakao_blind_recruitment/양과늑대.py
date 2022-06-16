from collections import defaultdict

def solution(info, edges):
    global tree, answer, visited
    
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
    
    answer = 0
    visited = [0] * len(info)
    visited[0] = 1
    def dfs(node, sheep, wolf):
        global answer
        
        if info[node] == 0:
            sheep += 1
            answer = max(sheep, answer)
        else:
            wolf += 1
            if wolf >= sheep:
                return
            
        for i in range(len(visited)):
            if visited[i] == 1:
                child = tree[i]
                for c in child:
                    if visited[c] == 0:
                        visited[c] = 1
                        dfs(c, sheep, wolf)
                        visited[c] = 0
        return
    
    dfs(0, 0, 0)
    return answer

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info, edges))