package main

func numberOfPairs(nums []int) (ans []int) {
	pairs := 0
	remains := 0
	m := map[int]bool{}
	for _, num := range nums {
		if m[num] {
			remains--
			pairs++
			m[num] = false
		} else {
			remains++
			m[num] = true
		}
	}
	ans = append(ans, pairs)
	ans = append(ans, remains)
	return
}

// func main() {
// 	nums := []int{1, 3, 2, 1, 3, 2, 2}
// 	fmt.Printf("numberOfPairs(nums): %v\n", numberOfPairs(nums))
// }
