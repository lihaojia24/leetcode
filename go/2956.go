package main

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	s1 := map[int]int{}
	s2 := map[int]int{}
	for _, num := range nums1 {
		s1[num] = 1
	}
	for _, num := range nums2 {
		s2[num] = 1
	}
	ans := [2]int{}
	for _, num := range nums1 {
		ans[0] += s2[num]
	}
	for _, num := range nums2 {
		ans[1] += s1[num]
	}
	return ans[:]
}
