function solution(arr){
    let answer = [];
    for(i=0; i<arr.length; i++){
        arr[i] == arr[i-1] ? answer.slice(arr[i],1) : answer.push(arr[i])
    }  
    return answer;
}