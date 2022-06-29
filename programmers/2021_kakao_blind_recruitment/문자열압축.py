def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        cut = s[:i]
        
        result = ''
        count = 1
        for j in range(i, len(s), i):
            cuting = s[j:j+i]
            if cuting == cut:
                count += 1
            else:
                if count == 1:
                    result += cut
                else:
                    result += str(count) + cut
                cut = cuting
                count = 1
        
        if count == 1:
            result += cuting
        else:
            result += str(count) + cuting
        
        answer = min(answer, len(result))

    return answer


s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"

print(solution(s))