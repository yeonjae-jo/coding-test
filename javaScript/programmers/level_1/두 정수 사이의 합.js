function solution(a, b) {
    let sum = 0;
    for(i=Math.min(a,b); i<=Math.max(a,b); i++)
    sum +=i;
    
    return sum;
}