function solution(n) {
    let answer= []
    for(i=2; i<n; i++){
        if(n%i == 1) answer.push(i)
    }
    return answer[0]
}