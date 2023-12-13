package main

func secondGreaterElement(nums []int) []int {
	s1 := []int{}
	s2 := []int{}
	ans := make([]int, len(nums))
	for i := range ans {
		ans[i] = -1
	}
	for i, num := range nums {
		for len(s2) > 0 && num > nums[s2[len(s2)-1]] {
			ans[s2[len(s2)-1]] = num
			s2 = s2[:len(s2)-1]
		}
		x := len(s1) - 1
		for x >= 0 && num > nums[s1[x]] {
			x--
		}
		s2 = append(s2, s1[x+1:]...)
		s1 = append(s1[:x+1], i)
	}
	return ans
}
