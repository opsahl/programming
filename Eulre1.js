// Solving Project euler problem 1 in javascript

function solve(max){
    var sum = 0;

    for(var i = 0; i < max; i++){
        if(i % 3 === 0 || i % 5 === 0){
            sum += i;
        }
    }

    return sum;
}

console.log(solve(10));
console.log(solve(1000));
