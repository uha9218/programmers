def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else :
            if not stack:
                return False
            stack.pop()
    if len(stack) !=0 :
        return False
    return True