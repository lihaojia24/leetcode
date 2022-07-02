package main

import (
	"container/heap"
	"fmt"
	"sort"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// dp
func minRefuelStops1(target int, startFuel int, stations [][]int) int {
	n := len(stations) + 1
	dp := make([]int, n)
	dp[0] = startFuel
	// dp = append(dp, startFuel)
	for i := 0; i < len(stations); i++ {
		for j := i + 1; j > 0; j-- {
			if dp[j-1] >= stations[i][0] {
				dp[j] = max(dp[j], dp[j-1]+stations[i][1])
			}
		}
	}
	for i := 0; i < len(dp); i++ {
		if dp[i] >= target {
			return i
		}
	}
	return -1
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{} {
	a := h.IntSlice
	v := a[len(a)-1]
	h.IntSlice = a[:len(a)-1]
	return v
}

// greedy
func minRefuelStops(target int, startFuel int, stations [][]int) int {
	fuel := startFuel
	step := 0
	h := hp{}
	for i := 0; i <= len(stations); {
		if i < len(stations) && fuel >= stations[i][0] {
			heap.Push(&h, stations[i][1])
			i++
		} else if i == len(stations) && fuel >= target {
			return step
		} else {
			if h.Len() > 0 {
				step++
				fuel += heap.Pop(&h).(int)
			} else {
				return -1
			}
		}
	}
	return step
}

func main() {
	target := 100
	startFuel := 50
	stations := [][]int{}

	stations = append(stations, []int{25, 50})
	stations = append(stations, []int{50, 25})
	// stations = append(stations, []int{10, 60})
	// stations = append(stations, []int{20, 30})
	// stations = append(stations, []int{30, 30})
	// stations = append(stations, []int{60, 40})

	// stations = append(stations, []int{25, 27})
	// stations = append(stations, []int{36, 187})
	// stations = append(stations, []int{140, 186})
	// stations = append(stations, []int{378, 6})
	// stations = append(stations, []int{492, 202})
	// stations = append(stations, []int{517, 89})
	// stations = append(stations, []int{579, 234})
	// stations = append(stations, []int{673, 86})
	// stations = append(stations, []int{808, 53})
	// stations = append(stations, []int{954, 49})
	fmt.Printf("minRefuelStops(target, startFuel, stations): %v\n", minRefuelStops(target, startFuel, stations))
}
