package main

import "fmt"

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func isGoodArray(nums []int) bool {
	g := nums[0]
	for i := 1; i < len(nums); i++ {
		g = gcd(g, nums[i])
		if g == 1 {
			return true
		}
	}
	return g == 1
}

func main() {
	nums := []int{12, 8}
	fmt.Printf("isGoodArray(nums): %v\n", isGoodArray(nums))
}
