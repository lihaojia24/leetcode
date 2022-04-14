package main

import "fmt"

func maximumWealth(accounts [][]int) int {
	ans := 0
	for _, account := range accounts {
		sum := 0
		for _, val := range account {
			sum += val
		}
		if sum > ans {
			ans = sum
		}
	}
	return ans
}

func main() {
	accounts := make([][]int, 3)
	for i := 0; i < 3; i++ {
		accounts[i] = []int{i + 1, i + 2, i + 3}
	}
	fmt.Printf("accounts: %v\n", accounts)
	ans := maximumWealth(accounts)
	fmt.Printf("ans: %v\n", ans)
}
