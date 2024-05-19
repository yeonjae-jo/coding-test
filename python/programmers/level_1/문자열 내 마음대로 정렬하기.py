def solution(strings, n):
    # sorted_arr = sorted(strings, key=lambda x:x[n])
    sorted_arr = sorted(strings, key=lambda x: (x[n], x))
    return sorted_arr
