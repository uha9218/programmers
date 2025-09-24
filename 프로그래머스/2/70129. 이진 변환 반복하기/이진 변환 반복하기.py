def solution(s):
    remove_count = 0
    change_count = 0
    while(s != "1"):
        before_s_length = len(s)
        s = s.replace("0","")
        remove_count += before_s_length - len(s)
        s = str(bin(len(s))).replace("0b","")
        change_count += 1
    answer = [change_count, remove_count]
    return answer