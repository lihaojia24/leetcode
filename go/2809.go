package main

import (
	"fmt"
	"sort"
)

func minimumTime(nums1 []int, nums2 []int, x int) int {
	s1, s2, n := 0, 0, len(nums1)
	id := make([]int, n)
	for i := range id {
		id[i] = i
		s1 += nums1[i]
		s2 += nums2[i]
	}
	sort.Slice(id, func(i, j int) bool { return nums2[id[i]] < nums2[id[j]] })
	// slices.SortFunc(id, func(i, j int) int { return nums2[i] - nums2[j] })
	fmt.Printf("id: %v\n", id)

	res := make([]int, n+1)
	for useIndex, rankIndex := range id {
		num1, num2 := nums1[rankIndex], nums2[rankIndex]
		for usedNum := useIndex + 1; usedNum > 0; usedNum-- {
			res[usedNum] = max(res[usedNum], res[usedNum-1]+num1+num2*usedNum)
		}
	}

	for usedNum, maxReduce := range res {
		if s1+s2*usedNum-maxReduce <= x {
			return usedNum
		}
	}
	return -1
}

// func main() {
// 	nums1 := []int{4, 4, 9, 10}
// 	nums2 := []int{4, 4, 1, 3}
// 	x := 16
// 	minimumTime(nums1, nums2, x)
// }
