package main

import "fmt"

// func main() {
// 	nums := []int{0, 1, 2, 2, 4, 4, 1}
// 	fmt.Printf("mostFrequentEven(nums): %v\n", mostFrequentEven(nums))
// }

func mostFrequentEven(nums []int) int {
	m := map[int]int{}
	for _, num := range nums {
		if num%2 == 0 {
			m[num]++
		}
	}
	ans := -1
	max := 0
	fmt.Printf("m: %v\n", m)
	for k, v := range m {
		if ans == -1 || v > max || (v == max && k < ans) {
			ans = k
			max = v
		}
	}
	return ans
}
