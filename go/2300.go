package main

import "sort"

func successfulPairs(spells []int, potions []int, success int64) (ans []int) {
	sort.Ints(potions)
	var find func(spell int) int
	find = func(spell int) int {
		if int64(spell)*int64(potions[len(potions)-1]) < success {
			return len(potions)
		}
		l, r := 0, len(potions)-1
		for l < r {
			mid := (l + r) >> 1
			if int64(spell)*int64(potions[mid]) < success {
				l = mid + 1
			} else {
				r = mid
			}
		}
		return l
	}
	for _, spell := range spells {
		index := find(spell)
		ans = append(ans, len(potions)-index)
	}
	return
}
