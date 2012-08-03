package main

import (
    "io/ioutil"
    "fmt"
    "strings"
    "strconv"
)

func read_file(name string) string {
    result, err := ioutil.ReadFile(name)
    if err != nil { panic(err) }
    return string(result)
}

func parse(str string) []int64 {
    str_slice := strings.Split(str, "\n")
    shrt_slice := make([]string, 100)
    num_slice := make([]int64, 100)

    for _, v := range str_slice {
        shrt_slice = append(shrt_slice, v[0:11])
    }

    for _, v := range shrt_slice {
        num, err := strconv.ParseInt(v, 10, 64)
        if err != nil { panic(err) }
        num_slice = append(num_slice, num)
    }

    return num_slice
}


func main() {
    // Getting a string of the file's contents
    file_str := read_file("euler13.txt")
    // parse the string to get a slice of numbers
    //nums := parse(file_str)
    fmt.Println(parse(file_str))
}
