package main

// func main() {
// 	nums := "0122"
// 	fmt.Printf("digitCount(nums): %v\n", digitCount(nums))
// }

func digitCount(nums string) bool {
	length := len(nums)
	counts := make([]int, length)
	for i, ch := range nums {
		num := int(ch - '0')
		counts[num]--
		counts[i] += num
	}
	for _, c := range counts {
		if c != 0 {
			return false
		}
	}
	return true
}
