package main

import "fmt"

func numberOfLines(widths []int, s string) []int {
	const maxWidth = 100
	ans := 1
	cur := 0
	for _, ch := range s {
		w := widths[ch-'a']
		cur += w
		if cur > maxWidth {
			ans++
			cur = w
		}
	}
	return []int{ans, cur}
}

func main() {
	widths := []int{10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}
	S := "abcdefghijklmnopqrstuvwxyz"
	ans := numberOfLines(widths, S)
	fmt.Printf("ans: %v\n", ans)
}
