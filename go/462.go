package main

import (
	"sort"
)

func minMoves2(nums []int) (ans int) {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	left, right := 0, len(nums)-1
	for left < right {
		ans += nums[right] - nums[left]
		left++
		right--
	}
	return
}

// func main() {
// 	fmt.Printf("minMoves2([]int{1, 10, 2, 9}): %v\n", minMoves2([]int{1, 10, 2, 9}))
// }
