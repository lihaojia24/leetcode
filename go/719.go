package main

import "sort"

// func smallestDistancePair(nums []int, k int) int {
// 	sort.Ints(nums)
// 	return sort.Search(nums[len(nums)-1]-nums[0], func(i int) bool {
// 		cnt := 0
// 		left := 0
// 		for right := 0; right < len(nums); right++ {
// 			for nums[right]-nums[left] > i {
// 				left++
// 			}
// 			cnt += right - left
// 		}
// 		return cnt >= k
// 	})
// }

func smallestDistancePair(nums []int, k int) int {
	sort.Ints(nums)
	var count func(int) int
	count = func(i int) int {
		cnt := 0
		left := 0
		for right := 0; right < len(nums); right++ {
			for nums[right]-nums[left] > i {
				left++
			}
			cnt += right - left
		}
		return cnt
	}
	left, right := 0, nums[len(nums)-1]-nums[0]
	for left < right {
		mid := (left + right) / 2
		cnt := count(mid)
		if cnt < k {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}
