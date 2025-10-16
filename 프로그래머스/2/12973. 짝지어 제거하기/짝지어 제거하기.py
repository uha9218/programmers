def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
            continue
        else:
            stack.append(char)
    if stack:
        return 0
    else:
        return 1