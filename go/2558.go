package main

import (
	"container/heap"
	"math"
	"sort"
)

type hp struct {
	sort.IntSlice
}

func (h *hp) Less(i, j int) bool {
	return h.IntSlice[i] > h.IntSlice[j]
}

func (_ hp) Pop() (_ any) { return }

func (_ hp) Push(any) {}

func pickGifts(gifts []int, k int) (ans int64) {
	h := &hp{gifts}
	heap.Init(h)
	for k > 0 && h.IntSlice[0] > 1 {
		h.IntSlice[0] = int(math.Sqrt(float64(gifts[0])))
		heap.Fix(h, 0)
		k--
	}
	for _, x := range h.IntSlice {
		ans += int64(x)
	}
	return
}
