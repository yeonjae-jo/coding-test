def solution(s):
    answer = list(s.lower())
    if answer.count('p') == answer.count('y'):
        return True
    else:
        return False
