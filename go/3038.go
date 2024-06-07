package main

func maxOperations(nums []int) (ans int) {
	i := 0
	tmp := -1
	for i+1 < len(nums) {
		if tmp < 0 {
			tmp = nums[i] + nums[i+1]
			ans++
		} else if tmp == nums[i]+nums[i+1] {
			ans++
		} else {
			break
		}
		i += 2
	}
	return
}
