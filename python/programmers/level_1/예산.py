def solution(d, budget):
    apply_count = 0
    d.sort()
    for value in enumerate(d):
        req_money = value[1]
        if budget-req_money >= 0:
            budget = budget-req_money
            apply_count += 1
    return apply_count
