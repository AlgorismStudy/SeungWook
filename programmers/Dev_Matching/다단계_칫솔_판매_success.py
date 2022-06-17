def solution(enroll, referral, seller, amount):
    parent = {}
    for i, j in zip(enroll, referral):
        parent[i] = j

    money = {}
    for i, j in zip(enroll, [0]*len(enroll)):
        money[i] = j

    amount = [i*100 for i in amount]
    for i in range(len(seller)):
        own = amount[i] - (amount[i] // 10)
        yours = amount[i] // 10
        money[seller[i]] += own
        
        boss = parent[seller[i]]
        while boss != "-" and yours > 0:
            own = yours - (yours // 10)
            yours //= 10
            money[boss] += own
            boss = parent[boss]
    
    answer = list(money.values())
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