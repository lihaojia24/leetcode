package main

import "fmt"

func findTheWinner(n int, k int) int {
	// if n <= 1 {
	// 	return n
	// }
	// ans := (findTheWinner(n-1, k) + k) % n
	// if ans == 0 {
	// 	return n
	// } else {
	// 	return ans
	// }
	ans := 1
	for i := 1; i < n; i++ {
		ans = (ans + k) % (i + 1)
		if ans == 0 {
			ans = i + 1
		}
		fmt.Printf("ans: %v\n", ans)
	}

	if ans == 0 {
		return n
	} else {
		return ans
	}
}

func main() {
	fmt.Printf("findTheWinner(5, 2): %v\n", findTheWinner(5, 2))
}
