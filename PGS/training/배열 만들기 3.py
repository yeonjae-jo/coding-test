def solution(arr, intervals):
    answer = []
    
    for i in intervals: 
        numbers = arr[i[0]:i[1]+1]
        for j in numbers:
            answer.append(j)
            
    return answer