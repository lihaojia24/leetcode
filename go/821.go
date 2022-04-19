package main

import "fmt"

func shortestToChar(s string, c byte) []int {
	n := len(s)
	ans := make([]int, n)
	idx := -n
	for i, ch := range s {
		if byte(ch) == c {
			idx = i
		}
		ans[i] = i - idx
	}
	idx = 2 * n
	for i := n - 1; i >= 0; i-- {
		fmt.Printf("s[i]: %v\n", s[i])
		fmt.Printf("c: %v\n", c)
		if s[i] == c {
			idx = i
		}
		// fmt.Printf("idx: %v\n", idx)
		if idx-i < ans[i] {
			ans[i] = idx - i
		}
	}
	return ans
}

func main() {
	ans := shortestToChar("loveleetcode", 'e')
	fmt.Printf("ans: %v\n", ans)
}
