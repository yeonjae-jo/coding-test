def solution(my_string, queries):
    s = my_string
    for i in range(len(queries)):
        start, end = queries[i][0], queries[i][1]
        reversed_part = s[start:end+1][::-1]
        s = s[:start] + reversed_part + s[end+1:]
    return s
