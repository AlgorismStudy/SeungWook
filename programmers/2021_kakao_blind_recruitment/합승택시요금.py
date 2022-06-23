def solution(n, s, a, b, fares):
    moneys = [[20000001]*(n+1) for _ in range(n+1)]
    for start, end, money in fares:
        moneys[start][end] = money
        moneys[end][start] = money
    
    for i in range(1, n+1):
        moneys[i][i] = 0
        
    for leg in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if moneys[start][leg] + moneys[leg][end] < moneys[start][end]:
                    moneys[start][end] = moneys[start][leg] + moneys[leg][end]
    
    answer = 20000001
    for i in range(1, n+1):
        if answer > moneys[s][i] + moneys[i][b] + moneys[i][a]:
            answer = moneys[s][i] + moneys[i][b] + moneys[i][a]
            
    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], 
         [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n, s, a, b = 7, 3, 4, 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n, s, a, b = 6, 4, 5, 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n, s, a, b, fares))