# Just testing coffeescript with a little fizzing and buzzing
test = (max)->
    for num in [1..max]
        if num % 3 is 0 and num % 5 is 0
            console.log "FizzBuzz"
            continue
        if num % 3 is 0
            console.log "Fizz"
            continue
        if num % 5 is 0
            console.log "Buzz"
            continue
        else
            console.log num
            continue

test(50)
