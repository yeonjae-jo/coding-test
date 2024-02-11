def solution(str_list, ex):
    str_list = [i for i in str_list if ex not in i]
    answer = "".join(str_list)
    return answer