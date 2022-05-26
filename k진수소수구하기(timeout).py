# import string

# tmp = string.digits
# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    result = ""
    while n:
        result = str(n % k) + result
        n = n // k
    arr = result.split('0')

    answer = 0
    for i in arr:
        if i != '1' and i != '' and prime_number(int(i)):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))