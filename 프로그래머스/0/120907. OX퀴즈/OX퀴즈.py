def solution(quizzes):
    answer = []
    for quize in quizzes:
        number1, operator, number2, tmp, result = quize.split(" ")
        if operator == "+" :
            if int(number1) + int(number2) == int(result) :
                answer.append("O")
            else : 
                answer.append("X")
        else:
            if int(number1) - int(number2) == int(result) :
                answer.append("O")
            else : 
                answer.append("X")
    return answer