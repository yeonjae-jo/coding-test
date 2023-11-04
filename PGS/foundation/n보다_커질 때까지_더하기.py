def solution(numbers, n):
    sum = 0
    for i in range(len(numbers)):
        if sum <= n:
            sum += numbers[i]
    return sum