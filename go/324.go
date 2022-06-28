package main

import (
	"fmt"
	"sort"
)

func quickSelect(nums []int, start int, end int, target int) {
	if start >= end {
		return
	}
	// fmt.Printf("start: %v\n", start)
	// fmt.Printf("end: %v\n", end)
	index := start
	tmp := nums[end]
	for i := start; i <= end; i++ {
		if nums[i] <= tmp {
			nums[index], nums[i] = nums[i], nums[index]
			index++
		}
	}
	fmt.Printf("index: %v\n", index)
	if index-1 > target {
		quickSelect(nums, start, index-2, target)
	} else {
		quickSelect(nums, index-1, end, target)
	}
}

func wiggleSort(nums []int) {
	sSize := len(nums) / 2
	if len(nums)%2 == 1 {
		sSize++
	}
	quickSelect(nums, 0, len(nums)-1, sSize)
	small := make([]int, sSize)
	big := make([]int, len(nums)-sSize)
	for i := 0; i < len(nums); i++ {
		if i < sSize {
			small[i] = nums[i]
		} else {
			big[i-sSize] = nums[i]
		}
	}
	fmt.Printf("small: %v\n", small)
	fmt.Printf("big: %v\n", big)
	smallIndex := len(small) - 1
	bigIndex := len(big) - 1
	for i := 0; i < len(nums); i++ {
		if i%2 == 0 {
			nums[i] = small[smallIndex]
			smallIndex--
		} else {
			nums[i] = big[bigIndex]
			bigIndex--
		}
	}
}

func wiggleSort2(nums []int) {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	sSize := len(nums) / 2
	if len(nums)%2 == 1 {
		sSize++
	}
	small := make([]int, sSize)
	big := make([]int, len(nums)-sSize)
	for i := 0; i < len(nums); i++ {
		if i < sSize {
			small[i] = nums[i]
		} else {
			big[i-sSize] = nums[i]
		}
	}
	fmt.Printf("small: %v\n", small)
	fmt.Printf("big: %v\n", big)
	smallIndex := len(small) - 1
	bigIndex := len(big) - 1
	for i := 0; i < len(nums); i++ {
		if i%2 == 0 {
			nums[i] = small[smallIndex]
			smallIndex--
		} else {
			nums[i] = big[bigIndex]
			bigIndex--
		}
	}
}

func main() {
	nums := []int{1, 5, 1, 1, 6, 4, 9}
	wiggleSort(nums)
	fmt.Printf("nums: %v\n", nums)
}
