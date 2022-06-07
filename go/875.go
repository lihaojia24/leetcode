package main

import "fmt"

func minEatingSpeed(piles []int, h int) int {
	left, right := 1, 1
	for _, v := range piles {
		if v > right {
			right = v
		}
	}
	var countTime func(speed int) int
	countTime = func(speed int) int {
		ans := 0
		for _, v := range piles {
			ans += (v + speed - 1) / speed
		}
		fmt.Printf("speed: %v\n", speed)
		fmt.Printf("ans: %v\n", ans)
		return ans
	}
	var mid int
	for left < right {
		mid = (left + right) / 2
		if countTime(mid) <= h {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func main() {
	piles := []int{3, 6, 7, 11}
	h := 8
	fmt.Printf("minEatingSpeed(piles, h): %v\n", minEatingSpeed(piles, h))
}
