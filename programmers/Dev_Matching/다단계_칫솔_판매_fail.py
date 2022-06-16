def solution(enroll, referral, seller, amount):
    parent = {}
    for i, j in zip(enroll, referral):
        parent[i] = j
    
    sell = {}
    for i, j in zip(seller, amount):
        sell[i] = j * 100
    print(sell)
    
    money = {}
    for i, j in zip(enroll, [0]*len(enroll)):
        money[i] = j

    
    for i in sell:
        own = sell[i] - (sell[i] // 10)
        yours = sell[i] // 10
        money[i] += own
        
        while parent[i] != "-":
            own = yours - (yours // 10)
            yours //= 10
            money[parent[i]] += own
            parent[i] = parent[parent[i]]

    answer = list(money.values())
    print(answer)
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary", "young"]
amount = [12, 4, 2, 5, 10, 12]

# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["sam", "emily", "jaimie", "edward"]
# amount = [2, 3, 5, 4]

solution(enroll, referral, seller, amount)