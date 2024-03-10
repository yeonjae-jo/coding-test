function solution(x) {
    let num = x;
    let sum = x.toString().split('').map(v => Number(v)).reduce((a,c) => a = a+c);
  
   return num % sum === 0 ? true : false;
 }