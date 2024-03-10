def solution(num_list):
    x, y = num_list[-1], num_list[-2]    
    num_list.append(x - y) if x > y else num_list.append(x * 2)
        
    return num_list