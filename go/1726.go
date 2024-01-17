package main

func tupleSameProduct(nums []int) int {
	// var m map[int]int
	m := map[int]int{}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			m[nums[i]*nums[j]]++
		}
	}
	ans := 0
	for _, v := range m {
		ans += v * (v - 1) / 2
	}
	return ans << 3
}
