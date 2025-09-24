def solution(my_string):
    answer = 0
    tmp = ""
    for part in my_string:
        if part.isdigit():
            tmp += part
        else:
            if tmp:
                answer += int(tmp)
            tmp=""
    if tmp:
        answer += int(tmp)
    return answer