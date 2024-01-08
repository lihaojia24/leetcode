package main

import (
	"fmt"
	"math/rand"
)

type RandomizedSet struct {
	nums    []int
	indices map[int]int
}

func cConstructor() RandomizedSet {
	return RandomizedSet{[]int{}, map[int]int{}}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.indices[val]; ok {
		return false
	}
	this.indices[val] = len(this.nums)
	this.nums = append(this.nums, val)
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if id, ok := this.indices[val]; ok {
		this.nums[id] = this.nums[len(this.nums)-1]
		this.indices[this.nums[id]] = id
		this.nums = this.nums[:len(this.nums)-1]
		delete(this.indices, val)
		return true
	}
	return false
}

func (this *RandomizedSet) GetRandom() int {
	l := len(this.nums)
	fmt.Printf("l: %v\n", l)
	return this.nums[rand.Intn(len(this.nums))]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */

// func main() {
// 	obj := Constructor()
// 	param_0 := obj.Insert(0)
// 	param_1 := obj.Insert(1)
// 	param_2 := obj.Remove(1)
// 	param_3 := obj.GetRandom()
// 	fmt.Printf("param_0: %v\n", param_0)
// 	fmt.Printf("param_1: %v\n", param_1)
// 	fmt.Printf("param_2: %v\n", param_2)
// 	fmt.Printf("param_3: %v\n", param_3)
// }
