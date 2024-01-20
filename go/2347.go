package main

import "bytes"

func bestHand(ranks []int, suits []byte) string {
	if bytes.Count(suits, suits[:1]) == 5 {
		return "Flush"
	}
	m := map[int]int{}
	pair := false
	for _, rank := range ranks {
		m[rank]++
		if m[rank] == 3 {
			return "Three of a Kind"
		}
		if m[rank] == 2 {
			pair = true
		}
	}
	if pair {
		return "Pair"
	}
	return "High Card"
}
