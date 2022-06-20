from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    order_dict = defaultdict(int)
    max_dict = defaultdict(int)
    for order in orders:
        for i in range(len(course)):
            if len(order) < course[i]:
                continue
            for com in combinations(sorted(order), course[i]):
                combi = "".join(com)
                order_dict[combi] += 1
                if max_dict[course[i]] < order_dict[combi]:
                    max_dict[course[i]] = order_dict[combi]
    
    answer = []
    for co in course:
        for key, value in order_dict.items():
            if not max_dict[co] == 1 and len(key) == co and value == max_dict[co]:
                answer.append(key)
                
    answer = sorted(answer)
    return answer

# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

solution(orders, course)