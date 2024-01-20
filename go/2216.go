package main

func minDeletion(nums []int) (ans int) {
	for i := 0; i < len(nums)-1; {
		if nums[i] != nums[i+1] {
			i += 2
		} else {
			i++
			ans++
		}
	}
	if (len(nums)-ans)%2 == 1 {
		ans++
	}
	return
}

// func main() {
// 	nums := []int{1, 1, 2, 2, 3, 3, 3}
// 	fmt.Printf("minDeletion(nums): %v\n", minDeletion(nums))
// }
