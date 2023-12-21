package main

import "fmt"

func maximumSumOfHeights(maxHeights []int) int64 {
	n := len(maxHeights)
	preMax := make([]int, n)
	st := []int{-1}
	s := 0
	for i := 0; i < n; i++ {
		x := maxHeights[i]
		for len(st) > 1 && maxHeights[st[len(st)-1]] >= x {
			j := st[len(st)-1]
			st = st[:len(st)-1]
			s -= maxHeights[j] * (j - st[len(st)-1])
		}
		s += x * (i - st[len(st)-1])
		preMax[i] = s
		st = append(st, i)
	}

	posMax := make([]int, n)
	st = []int{n}
	s = 0
	for i := n - 1; i > -1; i-- {
		x := maxHeights[i]
		for len(st) > 1 && maxHeights[st[len(st)-1]] >= x {
			j := st[len(st)-1]
			st = st[:len(st)-1]
			s -= maxHeights[j] * (st[len(st)-1] - j)
		}
		s += x * (st[len(st)-1] - i)
		posMax[i] = s
		st = append(st, i)
	}

	ans := 0
	for i := 0; i < n; i++ {
		ans = max(ans, preMax[i]+posMax[i]-maxHeights[i])
	}
	fmt.Println(int(^uint(0) >> 1))
	return int64(ans)
}
