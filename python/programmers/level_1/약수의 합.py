def solution(num):
    numbers = []
    for i in range(1, num+1):
        if num % i == 0:
            numbers.append(i)

    return sum(numbers)
