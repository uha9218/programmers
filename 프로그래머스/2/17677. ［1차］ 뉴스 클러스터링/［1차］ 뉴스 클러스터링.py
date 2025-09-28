from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    for i in range(len(str1) - 1):
        pair = str1[i:i+2]
        if pair.isalpha():
            str1_list.append(pair)
            
    for i in range(len(str2) - 1):
        pair = str2[i:i+2]
        if pair.isalpha():
            str2_list.append(pair)
            
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    
    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(union) == 0:
        return 65536
    else:
        return int(65536 * len(intersection) / len(union))