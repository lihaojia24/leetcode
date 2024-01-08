package main

import (
	"fmt"
	"math/rand"
)

type pair struct{ area, x, y, width, size int }

type Solution []pair

func Constructor(rects [][]int) Solution1 {
	s := Solution1{}
	area := 0
	for _, rect := range rects {
		size := (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
		area += size
		s = append(s, pair{area, rect[0], rect[1], rect[2] - rect[0] + 1, size})
	}
	return s
}

func (this Solution1) Pick() []int {
	area_max := this[len(this)-1].area
	k := rand.Intn(area_max)
	left, right := 0, len(this)-1
	for left < right {
		mid := (left + right) / 2
		if this[mid].area < k {
			left = mid + 1
		} else {
			right = mid
		}
	}
	p := this[left]
	fmt.Printf("k: %v\n", k)
	fmt.Printf("p: %v\n", p)
	index := (k - p.area + p.size)
	fmt.Printf("index: %v\n", index)
	x := index%p.width + p.x
	y := index/p.width + p.y
	return []int{x, y}
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(rects);
 * param_1 := obj.Pick();
 */

func main() {
	rects := make([][]int, 0)
	rects = append(rects, []int{-2, -2, 1, 1})
	rects = append(rects, []int{2, 2, 4, 6})
	s := Constructor(rects)
	p := s.Pick()
	fmt.Printf("p: %v\n", p)
	p = s.Pick()
	fmt.Printf("p: %v\n", p)
}
