package main

import "sort"

func maxSatisfaction(satisfaction []int) int {
	sort.Slice(satisfaction, func(i, j int) bool {
		return satisfaction[i] > satisfaction[j]
	})
	ans := 0
	total := 0
	for _, score := range satisfaction {
		total += score
		if total > 0 {
			ans += total
		} else {
			break
		}
	}
	return ans

}

func main() {

}
