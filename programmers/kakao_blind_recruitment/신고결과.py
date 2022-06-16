id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi","muzi neo"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

def solution(id_list, report, k):
    reporting = {}
    reported = {}
    for i in id_list:
        reporting[i], reported[i] = 0, 0
    
    report = set(report)
    for j in report:
        reported[j.split()[1]] += 1
    
    for re in reported:
        if reported[re] >= k:
            for r in report:
                if r.split()[1] == re:
                    reporting[r.split()[0]] += 1
    
    answer = []
    for i in reporting.values():
        answer.append(i)
    print(answer)
    return answer

solution(id_list, report, k)