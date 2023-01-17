package main

import "fmt"

func main() {
	nums := []int{13, 10, 35, 24, 76}
	fmt.Printf("countNicePairs(nums): %v\n", countNicePairs(nums))
}

func countNicePairs(nums []int) int {
	renums := []int{}
	for _, num := range nums {
		renums = append(renums, reverse(num))
	}
	m := map[int]int{}
	for i := 0; i < len(nums); i++ {
		m[nums[i]-renums[i]]++
	}
	ans := 0
	for _, v := range m {
		ans += v * (v - 1) / 2
		ans %= (1e9 + 7)
	}
	return ans
}

func reverse(num int) int {
	res := 0
	for num > 0 {
		res *= 10
		res += num % 10
		num /= 10
	}
	return res
}
