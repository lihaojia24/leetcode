package main

import (
	"fmt"
	"strconv"
)

func maximumSwap(num int) int {
	nums := []byte(strconv.Itoa(num))
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] <= nums[i+1] {
			mxj := i + 1
			for j := i + 1; j < len(nums); j++ {
				if nums[j] >= nums[mxj] {
					mxj = j
				}
			}
			l, r := 0, i
			fmt.Printf("r: %v\n", r)
			for l < r {
				m := (l + r) / 2
				if nums[m] >= nums[mxj] {
					l = m + 1
				} else {
					r = m
				}
			}
			fmt.Printf("l: %v\n", l)
			nums[l], nums[mxj] = nums[mxj], nums[l]
			break
		}
	}
	res, _ := strconv.Atoi(string(nums))
	return res
}

// func main() {
// 	num := 98368
// 	maximumSwap(num)
// }
