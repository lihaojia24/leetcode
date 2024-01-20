package main

import (
	"container/heap"
)

// type hp struct{ sort.IntSlice }

// func (h *hp) Push(v any) { h.IntSlice = append(h.IntSlice, v.(int)) }

// func (h *hp) Pop() any {
// 	a := h.IntSlice
// 	v := a[len(a)-1]
// 	h.IntSlice = a[:len(a)-1]
// 	return v
// }

type SmallestInfiniteSet struct {
	minNum  int
	others  hp
	othersM map[int]struct{}
}

func Constructor() SmallestInfiniteSet {
	return SmallestInfiniteSet{othersM: map[int]struct{}{}}
}

func (s *SmallestInfiniteSet) PopSmallest() int {
	if len(s.others.IntSlice) > 0 {
		v := heap.Pop(&s.others).(int)
		delete(s.othersM, v)
		return v
	} else {
		s.minNum++
		return s.minNum
	}
}

func (s *SmallestInfiniteSet) AddBack(num int) {
	if num <= s.minNum {
		if _, ok := s.othersM[num]; !ok {
			heap.Push(&s.others, num)
			s.othersM[num] = struct{}{}
		}
	}
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.PopSmallest();
 * obj.AddBack(num);
 */
