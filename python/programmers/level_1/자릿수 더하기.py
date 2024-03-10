def solution(n):
    nList = list(str(n))
    answer = []
    [answer.append(int(i)) for i in nList]

    return sum(answer)
