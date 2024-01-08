package main

import (
	"fmt"
	"math/rand"
)

type Solution struct {
	m     map[int]int
	bound int
}

func Constructor(n int, blacklist []int) Solution1 {
	m := len(blacklist)
	bound := n - m
	black := map[int]bool{}
	for _, b := range blacklist {
		if b >= bound {
			black[b] = true
		}
	}

	b2w := make(map[int]int, m-len(black))
	w := bound
	for _, b := range blacklist {
		if b < bound {
			for black[w] {
				w++
			}
			b2w[b] = w
			w++
		}
	}
	return Solution1{b2w, bound}
}

func (this *Solution1) Pick() int {
	x := rand.Intn(this.bound)
	if num, ok := this.m[x]; ok {
		return num
	}
	return x
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */

func main() {
	n := 6
	blacklist := []int{1, 2, 3}
	s := Constructor(n, blacklist)
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
	fmt.Printf("s.Pick(): %v\n", s.Pick())
}
