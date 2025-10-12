from collections import Counter
def solution(k, tangerine):
    answer = 0
    count_tan = Counter(tangerine).most_common()
    for size, tan in count_tan:
        k -= tan
        answer += 1
        if (k<=0) :
            break
    return answer