from collections import defaultdict
from itertools import combinations

def solution(info, query):
    user_dict = defaultdict(list)
    
    for user in info:
        user = user.split()
        key, value = user[:-1], user[-1]
        for i in range(5):
            for com in combinations(key, i):
                user_dict["".join(com)].append(value)
    
    for key in user_dict.keys():
        user_dict[key] = sorted(user_dict[key])
    
    answer = []
    for q in query:
        q = q.replace('-', '').replace(' and ', '').split()
        if len(q) == 1:
            q.insert(0, '')
        if q[0] in user_dict:
            result = 0
            for score in user_dict[q[0]]:
                if int(score) >= int(q[-1]):
                    result += 1
            answer.append(result)
            
    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))