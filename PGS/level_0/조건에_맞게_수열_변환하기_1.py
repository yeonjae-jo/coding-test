def solution(arr):
    answer = []
    for v in arr:        
        if(v >= 50 and v % 2 == 0): 
            answer.append(int(v / 2))
        elif(v <= 50 and v % 2 != 0): 
            answer.append(v * 2)
        else:
            answer.append(v)
            
    return answer