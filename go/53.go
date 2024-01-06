package main

func maxSubArray(nums []int) int {
	pre := nums[0]
	ans := pre
	for i := 1; i < len(nums); i++ {
		if pre < 0 {
			pre = nums[i]
		} else {
			pre += nums[i]
		}
		ans = max(pre, ans)
	}
	return ans
}

// func main() {

// }
