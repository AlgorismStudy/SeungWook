import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-zA-Z0-9-_.]', '', new_id)
    new_id = re.sub('\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    if new_id == "":
        new_id = "a"
    elif len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = re.sub('\.$', '', new_id)
    while len(new_id) < 3:
        new_id += new_id[-1]
            
    answer = new_id
    return answer
    

# new_id = "...!@BaT#*..y.abcdefghijklm."
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
# new_id = "abcdefghijklmn.p"
new_id = "=="

print(solution(new_id))