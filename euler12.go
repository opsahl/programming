package main

import "fmt"

// Function for finding number of divisors
func findDivisors(num int64) int64 {
    var divisors int64 = 0
    var limit int64 = num
    var i int64 = 1
    for ; i < limit; i++ {
        if num % i == 0 {
            limit = num / i
            divisors++
        }
    }

    return divisors * 2
}

// Generating new pyramid numbers
type Pyramid struct {
    Count, Number int64
}

func (p *Pyramid) next() int64 {
    p.Number += p.Count
    p.Count++
    return p.Number
}


func main() {

    Generator := Pyramid{1, 0}
    var divisors int64 = 0
    var pyramidNum int64 = 0

    for divisors < 500 {
        pyramidNum = Generator.next()
        // fmt.Printf("pyramid: %d, ", pyramidNum)
        divisors = findDivisors(pyramidNum)
        // fmt.Printf("divisors: %d\n", divisors)
    }

    fmt.Printf("%d\n", pyramidNum)

    // Commented out testing code
    /*
    fmt.Printf("Testing divisor finding\n")
    fmt.Printf("-----------------------\n")
    pyramids := []int{1, 3, 6, 10, 15, 21, 28}
    for _, v := range pyramids {
        fmt.Printf("%d: %d\n", v, findDivisors(v))
    }
    fmt.Println("Generating pyramid numbers")
    fmt.Println("--------------------------")
    Generator := Pyramid{1, 0}
    for i := 0; i < 10; i++ {
        fmt.Printf("%d\n", Generator.next())
    }
    */
}
