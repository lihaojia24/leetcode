package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func sum(nums []int) (ans int) {
	for _, num := range nums {
		ans += num
	}
	return
}

func findSubstringInWraproundString(p string) int {
	dp := [26]int{}
	dp[p[0]-'a'] = 1
	c := 1
	for i := 1; i < len(p); i++ {
		if (p[i]-p[i-1]+26)%26 == 1 {
			c++
		} else {
			c = 1
		}
		dp[p[i]-'a'] = max(dp[p[i]-'a'], c)
	}
	return sum(dp[:])
}

func main() {
	fmt.Printf("findSubstringInWraproundString(\"cac\"): %v\n", findSubstringInWraproundString("zab"))
	a := -9 % 7
	fmt.Printf("a: %v\n", a)
}
