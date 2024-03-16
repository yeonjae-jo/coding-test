function solution(arr, commands) {  
    let newArr = [], answer = [];
    for(let i=0; i<commands.length; i++){
        newArr = arr.slice(commands[i][0]-1, commands[i][1]).sort((a,b) => a - b);
        answer.push(newArr[commands[i][2]-1]);
    }
    return answer;
}