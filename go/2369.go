package main

func validPartition(nums []int) bool {
	if len(nums) < 2 {
		return false
	}
	n := len(nums)
	dp := make([]bool, n+1)
	dp[0] = true
	dp[1] = false
	dp[1+1] = nums[0] == nums[1]
	for i := range nums {
		if i > 1 {
			if nums[i] == nums[i-1] {
				if dp[i-2+1] {
					dp[i+1] = true
				} else if dp[i-3+1] && nums[i] == nums[i-2] {
					dp[i+1] = true
				}
			} else if nums[i] == nums[i-1]+1 && nums[i] == nums[i-2]+2 && dp[i-3+1] {
				dp[i+1] = true
			}
		}
	}
	return dp[n]
}
