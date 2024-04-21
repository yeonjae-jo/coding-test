def solution(s):
    answer = []
    arr = {}
    for idx, word in enumerate(s):
        if word not in arr:
            answer.append(-1)
            arr[word] = idx
        else:
            answer.append(idx-arr[word])
            arr[word] = idx
    return answer
