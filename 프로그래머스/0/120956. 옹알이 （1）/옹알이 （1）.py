def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        while True:
            is_matched = False
            for babble in can_speak:
                if word.startswith(babble):
                    word = word[len(babble):]
                    is_matched = True
                    break
            
            if not is_matched:
                break
        if len(word) == 0:
            answer += 1
    return answer
