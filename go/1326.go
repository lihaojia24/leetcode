package main

import (
	"fmt"
	"sort"
)

func minTaps(n int, ranges []int) (ans int) {
	m := map[int]int{}
	for i, v := range ranges {
		m[max(0, i-v)] = i + v
	}
	fmt.Printf("m: %v\n", m)
	tmp := 0
	loc := 0
	var keys []int
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, k := range keys {
		fmt.Printf("---\n")
		fmt.Printf("k: %v\n", k)
		fmt.Printf("v: %v\n", m[k])
		fmt.Printf("loc: %v\n", loc)
		fmt.Printf("tmp: %v\n", tmp)
		if k <= loc {
			tmp = max(tmp, m[k])
		} else {
			ans++
			loc = tmp
			tmp = -1
			fmt.Printf("k: %v\n", k)
			fmt.Printf("loc1: %v\n", loc)
			if loc >= n {
				return
			}
			if k <= loc {
				fmt.Printf("tmp11: %v\n", tmp)
				tmp = max(tmp, m[k])
			} else {
				return -1
			}
		}
	}
	if tmp >= n {
		ans++
		return
	} else {
		return -1
	}
}

// func main() {
// 	n := 35
// 	ranges := []int{1, 0, 4, 0, 4, 1, 4, 3, 1, 1, 1, 2, 1, 4, 0, 3, 0, 3, 0, 3, 0, 5, 3, 0, 0, 1, 2, 1, 2, 4, 3, 0, 1, 0, 5, 2}
// 	fmt.Printf("minTaps(n, ranges): %v\n", minTaps(n, ranges))
// }
