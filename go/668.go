package main

import "fmt"

func findKthNumber(m int, n int, k int) int {
	left, right := 0, m*n-1
	for left < right {
		mid := left + (left+right)/2
		count := mid / n * n
		for i := mid / n * n; i < m; i++ {
			count += mid / i
		}
		if count >= k {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func findKthNumberList(nums []int, num int) int {
	left, right := 0, len(nums)-1
	for left < right {
		fmt.Printf("left: %v\n", left)
		fmt.Printf("right: %v\n", right)
		mid := left + (right-left)/2
		if nums[mid] <= num {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	fmt.Printf("findKthNumberList(nums, 5): %v\n", findKthNumberList(nums, 9))
}
