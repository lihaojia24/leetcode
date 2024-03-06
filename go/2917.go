package main

func findKOr(nums []int, k int) (res int) {
	bitC := make([]int, 32)
	var bitCounts func(num int)
	bitCounts = func(num int) {
		for i := 0; num > 0; i++ {
			if num&1 > 0 {
				bitC[i]++
			}
			num >>= 1
		}
	}
	for _, num := range nums {
		bitCounts(num)
	}
	t := 1
	for _, c := range bitC {
		if c >= k {
			res += t
		}
		t <<= 1
	}
	return
}
