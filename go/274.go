package main

import "fmt"

func hIndex(citations []int) int {
	n := len(citations)
	cnt := make([]int, n+1)
	for _, t := range citations {
		if t > n {
			cnt[n]++
		} else {
			cnt[t]++
		}
	}
	fmt.Printf("cnt: %v\n", cnt)
	for i := n; i > 0; i-- {
		if cnt[i] >= i {
			return i
		} else {
			cnt[i-1] += cnt[i]
		}
	}
	return 0
}

func main() {

}
