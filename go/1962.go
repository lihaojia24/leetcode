package main

import (
	"container/heap"
	"sort"
)

func minStoneSum(piles []int, k int) int {
	h := &hp2{piles}
	heap.Init(h)
	for k > 0 && h.IntSlice[0] > 0 {
		h.IntSlice[0] -= h.IntSlice[0] / 2
		heap.Fix(h, 0)
		k--
	}
	ans := 0
	for _, x := range h.IntSlice {
		ans += x
	}
	return ans
}

type hp2 struct{ sort.IntSlice }

func (h *hp2) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] }
func (h *hp2) Push(v any)         { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp2) Pop() any {
	v := h.IntSlice[len(h.IntSlice)-1]
	h.IntSlice = h.IntSlice[:len(h.IntSlice)-1]
	return v
}
