devBy5n3 = (num)->
    if num % 3 is 0 or num % 5 is 0
        return true
    else
        return false

solve = (limit)->
    return (num for num in [1..(limit - 1)] when devBy5n3(num))

arr = solve(1000)

result = arr.reduce (x, y)-> x + y

console.log result
