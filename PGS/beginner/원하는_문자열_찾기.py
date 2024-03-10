def solution(myString, pat):   
    return 1 if myString.lower().count(pat.lower()) > 0 else 0 