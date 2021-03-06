def solution(lottos, win_nums):
    count = 0
    answer = 0
    for lotto in lottos:
        if lotto == 0:
            count += 1
        if lotto in win_nums:
            answer += 1
    return [min(7-(answer+count), 6), min(7 - answer, 6)]

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

lottos = [37, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]

# lottos = [45, 4, 35, 20, 3, 9]
# win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))