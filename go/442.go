package main

func findDuplicates(nums []int) (ans []int) {
	for _, num := range nums {
		if num < 0 {
			num = -num
		}
		if nums[num-1] < 0 {
			ans = append(ans, num)
		} else {
			nums[num-1] = -nums[num-1]
		}
	}
	return
}

// func main() {
// 	nums := []int{1, 1, 2, 3, 3, 4, 5, 2}
// 	fmt.Printf("findDuplicates(nums): %v\n", findDuplicates(nums))
// }
