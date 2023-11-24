package main

import (
	"sort"
)

func countPairs(nums []int, target int) int {
	ans := 0
	sort.Ints(nums)
	i := 0
	j := len(nums) - 1
	for i < j {
		if nums[i]+nums[j] >= target {
			j--
		} else {
			ans += j - i
			i++
		}
	}
	return ans
}

func countPairs2(nums []int, target int) int {
	ans := 0
	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		res := target - nums[i]
		ans += sort.SearchInts(nums[:i], res)
	}
	return ans
}

func main() {

}
