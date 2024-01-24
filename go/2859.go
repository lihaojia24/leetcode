package main

func sumIndicesWithKSetBits(nums []int, k int) (res int) {
	var bitCount func(int) int
	bitCount = func(num int) (cnt int) {
		for num > 0 {
			cnt++
			num -= num & ^(num - 1)
		}
		return
	}
	for i, num := range nums {
		if bitCount(i) == k {
			res += num
		}
	}
	return
}
