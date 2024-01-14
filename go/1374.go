package main

import "strings"

func generateTheString(n int) string {
	ans := strings.Repeat("a", n-1)
	if n%2 == 1 {
		ans = ans + "a"
	} else {
		ans = ans + "b"
	}
	return ans
}
