def solution(s):
    answer = 0
    index = 0  

    while index < len(s):
        
        x = s[index]
        count_x = 0
        count_other = 0

        for i in range(index, len(s)):
            if(s[i] == x) :
                count_x += 1
            else : 
                count_other += 1
            if count_x == count_other:
                break 
        
        answer += 1          
        index = i + 1        
        
    return answer