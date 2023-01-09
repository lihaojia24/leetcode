package main

import "fmt"

func main() {
	n := 6
	fmt.Printf("reinitializePermutation(n): %v\n", reinitializePermutation(n))
}

func reinitializePermutation(n int) int {
	step := 0
	index := 1
	for {
		step++
		if index < n/2 {
			index *= 2
		} else {
			index = (index-n/2)*2 + 1
		}
		if index == 1 {
			return step
		}
	}
}
