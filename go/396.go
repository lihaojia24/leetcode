package main

func maxRotateFunction(nums []int) (ans int) {
	numSum := 0
	tmp := 0
	n := len(nums)
	for i, num := range nums {
		numSum += num
		tmp += i * num
	}
	ans = tmp
	for i := range nums {
		if i == 0 {
			continue
		}
		tmp = tmp + numSum - n*nums[n-i]
		if tmp > ans {
			ans = tmp
		}
	}
	return
}
