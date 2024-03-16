function solution(s) {
    let answer = false;
    if(s.length === 4 || s.length === 6)
        answer = s.match(/[^0-9]/) === null ? true : false;

    return answer;
}