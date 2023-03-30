package main

import (
    "fmt"
    "math/rand"
    "time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

func main() {
    var arr[15000][15000]int

	start := time.Now()
	t := time.Now()
	elapsed := t.Sub(start)

	for i := 0; i < 15000; i++ {
		for j := 0; j < 15000; j++ {
			arr[i][j] = rand.Int()
		}
	}

	start = time.Now()
	for row := 0; row < 15000; row++ {
		for col := 0; col < 15000; col++ {
			arr[col][row] = rand.Int()
		}
	}
	t = time.Now()
	elapsed = t.Sub(start)
	fmt.Print("Col Major: ", elapsed, "\n")

	
	start = time.Now()
	for row := 0; row < 15000; row++ {
		for col := 0; col < 15000; col++ {
			arr[row][col] = rand.Int()
		}
	}
	t = time.Now()
	elapsed = t.Sub(start)
	fmt.Print("Row Major: ", elapsed, "\n")


	// Small experiment to show Go's memory model stores arrays in row-major order, same as C/C++
}

