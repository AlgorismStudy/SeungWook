def dfs(n, info, k, apeach, lion):
    global answer, max, temp
    if n == 0:
        if lion - apeach > max:
            max = lion - apeach
            answer = temp[:]
        elif lion - apeach == max and max != 0:
            for i in range(10, -1, -1):
                if temp[i] > answer[i]:
                    answer = temp[:]
                    break
                elif temp[i] < answer[i]:
                    break
        return

    for i in range(k, 11):
        if n > info[i]:
            temp[i] = info[i] + 1
            if info[i] > 0:
                dfs(n - temp[i], info, i + 1, apeach - (10 - i), lion + (10 - i))
            else:
                dfs(n - temp[i], info, i + 1, apeach, lion + (10 - i))
            temp[i] = 0
        else:
            if i == 10:
                temp[i] = n
                dfs(0, info, i + 1, apeach, lion)
                temp[i] = 0
            else:
                dfs(n, info, i + 1, apeach, lion)


def solution(n, info):
    global answer, max, temp
    answer = [0] * 11
    max = 0
    temp = [0] * 11
    
    apeach = 0 
    for i in range(11):
        if info[i] > 0:
            apeach += 10 - i
            
    dfs(n, info, 0, apeach, 0)
    
    if answer == [0] * 11:
        answer = [-1]
        
    return answer

# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

print(solution(n, info))