// Fizzing and buzzing with javascript

var fizzbuzz = function(max){
    for(var i = 1; i <= max; i++){
        if(i % 3 === 0){
            console.log("Fizz");
        } else if(i % 5 === 0) {
            console.log("Buzz");
        } else if(i % 3 === 0 && i % 5 === 0){
            console.log("FizzBuzz");
        } else {
            console.log(i);
        }
    } 
}

fizzbuzz(50);
