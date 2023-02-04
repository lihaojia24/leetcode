package main

import "sort"

func main() {

}

func getMaximumConsecutive(coins []int) int {
	// sort
	sort.Ints(coins)
	ans := 0
	for _, coin := range coins {
		if coin > ans+1 {
			return ans + 1
		}
		ans += coin
	}
	return ans + 1
}
