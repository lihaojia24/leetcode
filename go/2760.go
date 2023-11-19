package main

func longestAlternatingSubarray(nums []int, threshold int) (ans int) {
	for i := 0; i < len(nums); i++ {
		if nums[i] <= threshold && nums[i]%2 == 0 {
			t := 1
			for ; i+1 < len(nums); i++ {
				if nums[i+1] <= threshold && (nums[i]+nums[i+1])%2 == 1 {
					t++
				} else {
					break
				}
			}
			ans = max(ans, t)
		}
	}
	return
}

func main() {

}
