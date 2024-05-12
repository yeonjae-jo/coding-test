def solution(name, yearning, photo):
    answer = []
    # info = {}
    # for i, name in enumerate(name):
    #    info[name] = yearning[i]
    info = dict(zip(name, yearning))

    for people in photo:
        score = 0
        for person in people:
            score += info.get(person, 0)
        answer.append(score)
    return answer
