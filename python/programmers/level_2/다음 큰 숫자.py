def solution(n):
    nextN = n+1
    while True:
        if bin(nextN).count('1') == bin(n).count('1'):
            return nextN

        nextN += 1
