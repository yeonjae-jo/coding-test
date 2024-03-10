const solution = n => {
    let sum = [];
    for(let i = 1; i <= n; i++){
        if(n % i === 0) sum.push(i);
    }
    return sum.reduce((acc,cur) => acc += cur, 0);
}