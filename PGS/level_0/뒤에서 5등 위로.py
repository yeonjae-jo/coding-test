def solution(num_list):
    answer = []
    sortList = sorted(num_list)
    for i, v in enumerate(sortList):
        if i > 4:
            answer.append(v)
    return answer
