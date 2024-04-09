package main

func maximumCount1(nums []int) int {
	if nums[0] > 0 || nums[len(nums)-1] < 0 {
		return len(nums)
	}
	if nums[0] == 0 && nums[len(nums)-1] == 0 {
		return 0
	}
	pos, neg := 0, 0
	if nums[len(nums)-1] > 0 {
		l, r := 0, len(nums)-1
		for l < r {
			m := (l + r) / 2
			if nums[m] > 0 {
				r = m
			} else {
				l = m + 1
			}
		}
		pos = len(nums) - l
		// fmt.Printf("l: %v\n", l)
	}
	if nums[0] < 0 {
		l, r := 0, len(nums)-1
		for l < r {
			m := (l+r)/2 + 1
			if nums[m] < 0 {
				l = m
			} else {
				r = m - 1
			}
		}
		neg = l + 1
	}
	// fmt.Printf("neg: %v\n", neg)
	// fmt.Printf("pos: %v\n", pos)
	return max(neg, pos)
}

// func main() {
// 	nums := []int{-2, -1, -1, 1, 2, 3}
// 	fmt.Printf("maximumCount1(nums): %v\n", maximumCount1(nums))
// }
