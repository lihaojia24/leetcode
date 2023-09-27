package main

import "sort"

func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	ans := [][]int{}
	for _, res := range restaurants {
		can := true
		if veganFriendly == 1 {
			can = res[2] == 1
		}
		can = can && (maxPrice >= res[3])
		can = can && (maxDistance >= res[4])
		if can {
			ans = append(ans, []int{res[0], res[1]})
		}
	}
	sort.Slice(ans, func(i, j int) bool {
		if ans[i][1] == ans[j][1] {
			return ans[i][0] > ans[j][0]
		} else {
			return ans[i][1] > ans[j][1]
		}
	})
	t := []int{}
	for _, v := range ans {
		t = append(t, v[0])
	}
	return t
}
