def solution(str_list, ex):
    answer = ''
    for idx, val in enumerate(str_list):
        if (val.find(ex) == -1):
            answer += val
    return answer
