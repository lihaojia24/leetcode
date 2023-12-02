package main

import "sort"

func carPooling(trips [][]int, capacity int) bool {
	n := len(trips)
	actions := make([][2]int, 2*n)
	for i, trip := range trips {
		actions[2*i] = [2]int{trip[1], trip[0]}
		actions[2*i+1] = [2]int{trip[2], -trip[0]}
	}
	// actions := make([][2]int, 0)
	// for _, trip := range trips {
	// 	actions = append(actions, [2]int{trip[1], trip[0]})
	// 	actions = append(actions, [2]int{trip[2], -trip[0]})
	// }
	sort.Slice(actions, func(i, j int) bool {
		if actions[i][0] == actions[j][0] {
			return actions[i][1] < actions[j][1]
		}
		return actions[i][0] < actions[j][0]
	})
	passenger := 0
	for _, action := range actions {
		passenger += action[1]
		if passenger > capacity {
			return false
		}
	}
	return true
}
