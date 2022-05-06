package main

import "fmt"

func findTheWinner0(n int, k int) int {
	if n == 1 {
		return 0
	}
	return (findTheWinner0(n-1, k) + k) % n
}

func findTheWinner(n int, k int) int {
	return findTheWinner0(n, k) + 1
}

func main() {
	fmt.Printf("findTheWinner(5, 2): %v\n", findTheWinner(5, 2))
}
