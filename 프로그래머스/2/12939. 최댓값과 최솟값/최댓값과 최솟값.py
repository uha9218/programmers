def solution(s):
    answer = ''
    numbers = s.split(" ")
    max_num = int(numbers[0])
    min_num = int(numbers[0])
    for i in numbers:
        if max_num < int(i):
            max_num = int(i)
        
        if min_num > int(i):
            min_num = int(i)
    answer = str(min_num) + " " + str(max_num)
    return answer