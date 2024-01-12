package main

func sortArrayByParity(nums []int) []int {
	i, j := 0, len(nums)-1
	for i < j {
		if nums[i]%2 == 1 {
			nums[i], nums[j] = nums[j], nums[i]
			j--
		} else {
			i++
		}
	}
	return nums
}

// func main() {
// 	nums := []int{3, 1, 2, 4}
// 	ans := sortArrayByParity(nums)
// 	fmt.Printf("ans: %v\n", ans)
// }
