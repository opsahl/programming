solve = (max)->
    max -= 1
    nums = ( num for num in [1..max] when (num % 3 is 0 or num % 5 is 0))
    nums.reduce((x, y)-> x + y)

console.log solve(10)
console.log solve(1000)
