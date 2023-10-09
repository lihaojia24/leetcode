package main

import "sort"

func splitNum(num int) int {
	nums := []int{}
	for num > 0 {
		nums = append(nums, num%10)
		num /= 10
	}
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	ans := [2]int{}
	for i, v := range nums {
		ans[i%2] = ans[i%2]*10 + v
	}
	return ans[0] + ans[1]
}

func main() {

}
