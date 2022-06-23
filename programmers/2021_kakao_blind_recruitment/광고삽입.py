def t_to_s(t):
    num = t.split(':')
    return int(num[0])*3600 + int(num[1])*60 + int(num[2])

def s_to_t(s):
    num = ''
    num += str(s//3600).zfill(2)+':'
    s %= 3600
    num += str(s//60).zfill(2)+':'
    s %= 60
    num += str(s).zfill(2)
    return num

def solution(play_time, adv_time, logs):
    pt, at = t_to_s(play_time), t_to_s(adv_time)
    
    people_list = [0] * 360001
    for log in logs:
        start, end = map(t_to_s, log.split('-'))
        people_list[start] += 1
        people_list[end] -= 1
    
    for i in range(1, 360001):
        people_list[i] += people_list[i-1]
    
    start_time = 0
    max_people = sum(people_list[:at])
    tmp = max_people
    for i in range(1, 360001-at):
        tmp = tmp - people_list[i-1] + people_list[i+at-1]
        if tmp > max_people:
            max_people = tmp
            start_time = i
            
    return s_to_t(start_time)
    
# play_time = "02:03:55"
# adv_time = "00:14:15"
# logs = 	["01:20:15-01:45:14", "00:40:31-01:00:00", 
#          "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", 
#         "79:59:59-99:59:59", "11:00:00-31:00:00"]

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))
