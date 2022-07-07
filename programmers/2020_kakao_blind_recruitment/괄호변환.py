def is_correct(new_p):
        cnt = 0
        for j in new_p:
            if j == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0

def slice_p(p):
    l_count = 0
    r_count = 0
    new_p = []
    for i in range(len(p)):
        if p[i] == '(':
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            new_p = p[:i+1]
            l_p = p[i+1:]
            return new_p, l_p
        
def solution(p):
    if p == '':
        return p

    u, v = slice_p(p)
    if is_correct(u):
        return u + solution(v)
    
    answer = ''
    for i in u[1:-1]:
        answer += '(' if i == ')' else ')'
    
    return '(' + solution(v) + ')' + answer

    
# p = "(()())()"
# p = ")("
# p = "()))((()"
p = ")()(()"

print(solution(p))