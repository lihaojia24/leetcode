package main

import "fmt"

func quick_sort(nums []int, start, end int) {
	if start >= end {
		return
	}
	index, target := start, nums[end]
	for i := start; i <= end; i++ {
		if nums[i] <= target {
			nums[index], nums[i] = nums[i], nums[index]
			index++
		}
	}
	quick_sort(nums, start, index-2)
	quick_sort(nums, index-1, end)
}

func main() {
	nums := []int{6, 1, 18, 0, 1, 3, 2, 5, 1, 4, 6}
	quick_sort(nums, 0, len(nums)-1)
	fmt.Printf("nums: %v\n", nums)
}
