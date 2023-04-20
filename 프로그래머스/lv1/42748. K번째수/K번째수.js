function solution(array, commands) {
                 let answer = []
    commands.map((v,i)=>{
        let newArray = []

        let a =v[0]-1
        let b =v[1]
        let k =v[2]-1
        for (a;a<b;a++){
            newArray.push(array[a])
        }
        newArray.sort((a,b)=>(a-b))
        answer.push(newArray[k])
    })

    return answer;
}