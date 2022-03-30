import sys
input = sys.stdin.readline
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

while 1:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n, 2):
        if is_prime_number(i) == True and is_prime_number(n-i) == True:
            print(n,'=',i,'+',n-i)
            break