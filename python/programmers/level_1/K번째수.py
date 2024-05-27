def solution(array, commands):
    tmpArr = []
    answer = []
    for i in commands:
        x = list(array[i[0]-1:i[1]])
        x.sort()
        tmpArr.append(x)

    for j in range(len(tmpArr)):
        answer.append(tmpArr[j][commands[j][2]-1])
    return answer
