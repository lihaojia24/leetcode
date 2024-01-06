package main

import (
	"cmp"
	"slices"
	"sort"
)

func maximumSumQueries(nums1 []int, nums2 []int, queries [][]int) []int {
	type pair struct{ x, y int }
	a := make([]pair, len(nums1))
	for i, x := range nums1 {
		a[i] = pair{x, nums2[i]}
	}
	sort.SliceStable(a, func(i, j int) bool { return a[i].x >= a[j].x })
	qid := make([]int, len(queries))
	for i := range qid {
		qid[i] = i
	}
	slices.SortFunc(qid, func(i, j int) int { return cmp.Compare(queries[j][0], queries[i][0]) })
	ans := make([]int, len(queries))
	for i := range ans {
		ans[i] = -1
	}
	type data struct{ y, s int }
	st := []data{}
	j := 0
	for _, i := range qid {
		x, y := queries[i][0], queries[i][1]
		for ; j < len(a) && a[j].x >= x; j++ {
			ax, ay := a[j].x, a[j].y
			if len(st) == 0 {
				st = append(st, data{ay, ax + ay})
			} else if ay > st[len(st)-1].y {
				for len(st) > 0 && st[len(st)-1].s <= ax+ay {
					st = st[:len(st)-1]
				}
				st = append(st, data{ay, ax + ay})
			}
		}
		p := sort.Search(len(st), func(i int) bool { return st[i].y >= y })
		if p < len(st) {
			ans[i] = st[p].s
		}
	}
	return ans
}
