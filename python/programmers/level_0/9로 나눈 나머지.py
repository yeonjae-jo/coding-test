def solution(number):
    numbers = list(map(int,str(number)))
    return sum(numbers) % 9