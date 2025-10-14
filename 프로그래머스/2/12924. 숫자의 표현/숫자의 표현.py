def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        sum = 0
        for j in range(i, n):
            if sum > n:
                break
            else :
                sum += j
            
            if sum == n:
                answer += 1
                break
            
    
    return answer