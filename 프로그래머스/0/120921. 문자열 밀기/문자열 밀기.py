def solution(A, B):
    answer = 0
    for _ in range(len(A)):
        if A == B : 
            return answer
        A = A[-1] + A[0:-1]
        answer += 1
    answer = -1
    return answer