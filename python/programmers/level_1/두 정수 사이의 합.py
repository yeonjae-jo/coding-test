def solution(a, b):
    if b > a:
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))
