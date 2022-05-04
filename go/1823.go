package main

import "fmt"

func findTheWinner(n int, k int) int {
	ans := 0
	for i := 2; i < n+1; i++ {
		ans = (ans + k) % i
	}
	return ans + 1
}

func main() {
	fmt.Printf("findTheWinner(5, 2): %v\n", findTheWinner(5, 2))
}
