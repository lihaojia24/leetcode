package main

func distinctDifferenceArray(nums []int) []int {
	n := len(nums)
	dis_from_left := make([]int, n)
	dis_from_right := make([]int, n+1)
	s := map[int]struct{}{}
	dis := 0
	for i, num := range nums {
		if _, ok := s[num]; !ok {
			s[num] = struct{}{}
			dis++
		}
		dis_from_left[i] = dis
	}
	s = map[int]struct{}{}
	dis = 0
	for i := n - 1; i > -1; i-- {
		if _, ok := s[nums[i]]; !ok {
			s[nums[i]] = struct{}{}
			dis++
		}
		dis_from_right[i] = dis
	}
	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = dis_from_left[i] - dis_from_right[i+1]
	}
	return res
}
