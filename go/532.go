package main

func findPairs(nums []int, k int) (ans int) {
	m := map[int]int{}
	for _, num := range nums {
		if k == 0 {
			if m[num] == 1 {
				ans++
			}
		} else {
			if m[num] == 0 {
				if m[num-k] > 0 {
					ans++
				}
				if m[num+k] > 0 {
					ans++
				}
			}
		}
		m[num]++
	}
	return
}

// func main() {
// 	nums := []int{3, 1, 4, 1, 5}
// 	k := 2
// 	fmt.Printf("findPairs(nums, k): %v\n", findPairs(nums, k))
// }
