# 알고리즘 기법[전체 탐색] - 브루트 포스(brute force)
def solution(number):
    cnt, l = 0, len(number)
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if (number[i]+number[j]+number[k] == 0):
                    cnt += 1
    return cnt
