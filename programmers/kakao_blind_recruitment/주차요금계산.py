# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
#            "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
#            "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT",
           "18:00 0202 OUT","23:58 3961 IN"]

from collections import defaultdict
import math

def minutes(time):
    time = time.split(':')
    return 60 * int(time[0]) + int(time[1])

def solution(fees, records):
    car_minutes = defaultdict(list)
    for record in records:
        record = record.split()
        time = minutes(record[0])
        car_minutes[int(record[1])].append(time)
    
    answer = []
    for i in sorted(car_minutes.keys()):
        if len(car_minutes[i]) % 2:
            car_minutes[i].append(1439)
        
        total_time = 0
        for j in range(len(car_minutes[i])-1, -1, -2):
            total_time += car_minutes[i][j] - car_minutes[i][j-1]
        
        money = fees[1]
        if total_time > fees[0]:
            money += (math.ceil((total_time - fees[0]) / fees[2])) * fees[3]
            
        answer.append(money)
        
    print(answer)
    return answer

solution(fees, records)