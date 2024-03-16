function solution(l, r) {
    let arr = [], sum = 0;
        for(i=l; i<=r; i++){
            for(j=1; j<=i; j++){
                if(i%j === 0) 
                    arr.push(j);
            }
            sum = arr.length % 2 == 0 ? sum +=i : sum -= i;
            arr = []
        }
        return sum  
    }