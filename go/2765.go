package main

func alternatingSubarray(nums []int) int {
	t := -1
	mx := -1
	for i, num := range nums[:len(nums)-1] {
		if t == -1 {
			if nums[i+1] == num+1 {
				t = 2
			}
		} else {
			if nums[i+1] == nums[i-1] {
				t += 1
			} else if nums[i+1] == num+1 {
				t = 2
			} else {
				t = -1
			}
		}
		mx = max(mx, t)
	}
	return mx
}
