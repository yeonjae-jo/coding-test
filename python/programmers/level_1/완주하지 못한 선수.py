def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]
# def solution(participant, completion):
#    participant.sort()
#    completion.sort()
#    for i in range(0,len(completion)):
#        if participant[i] !=completion[i]:
#            return participant[i]
#    return participant[-1]
