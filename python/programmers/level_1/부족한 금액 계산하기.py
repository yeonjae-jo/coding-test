def solution(price, my_money, count):
    req_money = 0
    for i in range(1, count+1):
        req_money += price*i
    if req_money >= my_money:
        answer = req_money-my_money
    else:
        answer = 0
    return answer
