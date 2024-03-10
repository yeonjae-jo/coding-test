def solution(strArr):
    tmp = []
    # for i in strArr:
    #    answer.append(len(i))
    # 축약형으로 연습하기
    answer = [len(i) for i in strArr]

    for i in set(answer):
        tmp.append(answer.count(i))

    return max(tmp)
