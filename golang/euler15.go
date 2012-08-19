package main

import ("fmt"
        "math/big")

func factorial(upto *big.Int) *big.Int {
    factorial := big.NewInt(1)
    i := big.NewInt(1)
    for i; i <= upto; i++ {
        factorial = big.Int.Mul(i, factorial)
    }
    return factorial
}

func combinations(n, k *big.Int) *big.Int {
    return big.Int.Div(factorial(big.Int.Add(n, k), big.Int.Mul(factorial(n), factorial(k))))
}

func main() {
    i := big.NewInt(1);
    for i = 0; i <= 20; i++ {
        fmt.Println(combinations(i, i))
    }
}
