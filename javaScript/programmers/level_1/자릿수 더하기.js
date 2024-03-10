function solution(n){ 
    let number = n.toString().split('');
    number = number.map((v) => Number(v));
    
    return number.reduce((acc, cur) => acc += cur);
}