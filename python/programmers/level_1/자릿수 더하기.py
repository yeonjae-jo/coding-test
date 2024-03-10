def solution(n):
    nList = list(str(n))
    answer = []
    for i in nList:
        answer.append(int(i))

    return sum(answer)
