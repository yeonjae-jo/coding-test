const solution = (lottos, win_nums) => { 
    let rankArr = [6,6,5,4,3,2,1];
    let zeroCnt = lottos.filter((v) => v == 0).length;
    let okCnt = lottos.filter((v) => win_nums.includes(v)).length;
    
    return [rankArr[okCnt + zeroCnt], rankArr[okCnt]] 
}
