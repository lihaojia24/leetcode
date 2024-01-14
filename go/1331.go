package main

import "sort"

func arrayRankTransform(arr []int) []int {
	tArr := append([]int{}, arr...)
	sort.Ints(tArr)
	ranks := map[int]int{}
	rank := 1
	for _, v := range tArr {
		if _, ok := ranks[v]; !ok {
			ranks[v] = rank
			rank++
		}
	}
	ans := make([]int, len(arr))
	for i, v := range arr {
		ans[i] = ranks[v]
	}
	return ans
}
