package main

func numSubarrayProductLessThanK(nums []int, k int) (ans int) {
	tmp := 1
	start := 0
	for end, num := range nums {
		tmp *= num
		for start <= end && tmp >= k {
			tmp /= nums[start]
			start += 1
		}
		ans += end - start + 1
	}
	return
}

// func main() {
// 	nums := []int{10, 5, 2, 6}
// 	fmt.Printf("numSubarrayProductLessThanK(nums, 100): %v\n", numSubarrayProductLessThanK(nums, 100))
// }
