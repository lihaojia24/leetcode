package main

import (
	"fmt"
	"testing"
)

func fact(n int) int {
	if n == 1 {
		return 1
	} else {
		return n * fact(n-1)
	}
}

func Test_fact(t *testing.T) {
	fmt.Print("ss")
}

func main() {
	fmt.Printf("fact(3): %v\n", fact(3))
}
