fibsUpto = (limit)->
    list = [1]
    oldcurr = 0
    current = 1

    while current < limit
        list.push current
        temp = oldcurr
        oldcurr = current
        current = temp + current

    list 

result = (num for num in fibsUpto(4000000) when num % 2 is 0)
result = result.reduce (x, y)-> x+y
console.log result
