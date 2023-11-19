package main

import "fmt"

func maximumSum(nums []int) int {
	ans := -1
	var getPossum func(int) int
	getPossum = func(num int) (ans int) {
		for ; num > 0; num /= 10 {
			ans += num % 10
		}
		return ans
	}
	m := map[int]int{}
	for _, num := range nums {
		x := getPossum(num)
		s, ok := m[x]
		if ok {
			ans = max(ans, s+num)
			m[x] = max(s, num)
		} else {
			m[x] = num
		}
	}
	return ans
}

func main() {
	nums := []int{18, 43, 36, 13, 7}
	s := maximumSum(nums)
	fmt.Printf("s: %v\n", s)
}
