package main

func maxSlice(nums []int) (res int) {
	for _, num := range nums {
		res = max(res, num)
	}
	return
}

func splitArray(nums []int, k int) int {
	l := maxSlice(nums)
	r := sum(nums)
	for l < r {
		m := (l + r) / 2
		cnt := 1
		s := 0
		for _, num := range nums {
			if s+num > m {
				cnt++
				s = num
			} else {
				s += num
			}
		}
		if cnt > k {
			l = m + 1
		} else {
			r = m
		}
	}
	return l
}
