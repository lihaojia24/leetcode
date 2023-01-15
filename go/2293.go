package main

import "fmt"

func main() {
	nums := []int{1}
	fmt.Printf("minMaxGame(nums): %v\n", minMaxGame(nums))
}

func minMaxGame(nums []int) int {
	n := len(nums)
	flag := 1
	for n > 1 {
		n /= 2
		for i := 0; i < n; i++ {
			if i%2 == 1 {
				nums[i] = flag * min(flag*nums[2*i], flag*nums[2*i+1])
			} else {
				nums[i] = min(nums[2*i], nums[2*i+1])
			}
			flag *= -1
		}
	}
	return nums[0]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
