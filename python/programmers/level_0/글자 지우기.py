def solution(my_string, indices):
    answer = ''
    for idx, val in enumerate(my_string):
        if idx not in indices:
            answer += val
    return answer
