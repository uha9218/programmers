def solution(n):
    for num in range(n+1, 1000000):
        if(bin(num).count('1')==bin(n).count('1')):
            return num
    return 0