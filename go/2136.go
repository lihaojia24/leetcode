package main

import "sort"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func earliestFullBloom(plantTime []int, growTime []int) (ans int) {
	type pair struct{ p, g int }
	plants := make([]pair, len(plantTime))
	for i, p := range plantTime {
		plants[i] = pair{p, growTime[i]}
	}
	sort.Slice(plants, func(i, j int) bool {
		return plants[i].g > plants[j].g
	})
	days := 0
	for _, plant := range plants {
		days += plant.p
		ans = max(ans, days+plant.g)
	}
	return ans
}
