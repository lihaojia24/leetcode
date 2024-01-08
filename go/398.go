package main

import "math/rand"

type Solution1 struct {
	nums []int
}

func ccConstructor(nums []int) Solution1 {
	return Solution1{nums}
}

func (this *Solution1) Pick(target int) (ans int) {
	cnt := 0
	for i, num := range this.nums {
		if num == target {
			cnt++
			if rand.Intn(cnt) == 0 {
				ans = i
			}
		}
	}
	return
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.Pick(target);
 */
