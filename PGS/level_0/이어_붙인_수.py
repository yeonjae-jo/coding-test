def solution(num_list):  
    x, y = '', '' # 홀, 짝
    for i in num_list:
        if(i % 2 != 0):
            x += str(i)
        else:
            y += str(i)
            
    return int(x) + int(y)