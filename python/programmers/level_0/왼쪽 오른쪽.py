def solution(str_list):
    for idx, word in enumerate(str_list):
        if word == 'l':
            return str_list[:idx]
        elif word == 'r':
            return str_list[idx+1:]
    else:
        return []
