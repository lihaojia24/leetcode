package main

import (
	"fmt"
	"sort"
)

type num struct {
	value int
	tag   int
}

func main() {
	nums := []num{{1, 2}, {1, 3}, {0, 0}}
	sort.Slice(nums, func(i, j int) bool {
		return nums[i].value < nums[j].value
	})
	fmt.Printf("nums: %v\n", nums)
}
