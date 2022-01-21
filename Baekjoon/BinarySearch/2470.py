import sys

input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))

start = 0
end = N-1

big_number = 2000000000
new_start, new_end = start, end

while start < end:
    number = start + end
    if abs(number) < big_number:
        new_start, new_end = start, end
        big_number = abs(number)
        if big_number == 0:
            break
    if number > 0:
        end -= -1
    else:
        start += 1

array = [N_list[new_start], N_list[new_end]]
print(*sorted(array))