package main

import "sort"

// func sum(li []int) (ans int) {
// 	for _, v := range li {
// 		ans += v
// 	}
// 	return
// }

func minimumRemoval(beans []int) (res int64) {
	n, s := len(beans), int64(sum(beans))
	sort.Ints(beans)
	res = s
	for i, bean := range beans {
		x := s - int64(bean*(n-i))
		res = min(res, x)
	}
	return
}
