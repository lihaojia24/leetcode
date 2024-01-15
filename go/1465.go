package main

import "sort"

func getMax(size int, cuts []int) int {
	sort.Ints(cuts)
	res := max(cuts[0], size-cuts[len(cuts)-1])
	for i := 1; i < len(cuts); i++ {
		res = max(res, cuts[i]-cuts[i-1])
	}
	return res
}

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	h_max := getMax(h, horizontalCuts)
	v_max := getMax(w, verticalCuts)
	return (h_max * v_max) % 1_000_000_007
}
