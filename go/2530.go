package main

import (
	"container/heap"
)

type myHeap []int // Len is the number of elements in the collection.
func (h myHeap) Len() int {
	return len(h)
}

func (h myHeap) Less(i int, j int) bool {
	return h[i] > h[j]
}

func (h myHeap) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *myHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *myHeap) Pop() any {
	n := len(*h)
	x := (*h)[n-1]
	*h = (*h)[:n-1]
	return x
}

func maxKelements(nums []int, k int) int64 {
	q := (*myHeap)(&nums)
	heap.Init(q)
	var ans int64
	for i := 0; i < k; i++ {
		num := heap.Pop(q).(int)
		ans += int64(num)
		heap.Push(q, (num+2)/3)
	}
	return int64(ans)
}
