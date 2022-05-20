package main

import (
	"fmt"
	"sort"
)

func find2(nums []int, num int) (ans int) {
	left, right := 0, len(nums)
	for left < right {
		mid := left + (right-left)/2
		if nums[mid] < num {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func find(nums [][]int, num int) (ans int) {
	left, right := 0, len(nums)-1
	for left < right {
		mid := left + (right-left)/2
		if nums[mid][0] < num {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func findRightInterval(intervals [][]int) (ans []int) {
	// start, index
	m := [][]int{}
	for i, v := range intervals {
		m = append(m, []int{v[0], i})
	}
	sort.Slice(m, func(i, j int) bool {
		return m[i][0] < m[j][0]
	})
	for _, v := range intervals {
		right := v[1]
		// index := sort.Search(len(m), func(i int) bool {
		// 	return m[i][0] >= right
		// })
		index := find(m, right)
		if index < len(m) {
			ans = append(ans, m[index][1])
		} else {
			ans = append(ans, -1)
		}
	}
	return
}

func main() {
	nums := []int{1, 2, 3}
	ans := find2(nums, 3)
	fmt.Printf("ans: %v\n", ans)
}
