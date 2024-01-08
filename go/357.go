package main

func countNumbersWithUniqueDigits(n int) int {
	if n == 0 {
		return 1
	} else if n == 1 {
		return 10
	}
	var (
		ans = 10
		cur = 9
	)
	for i := 0; i < n-1; i++ {
		cur *= 9 - i
		ans += cur
	}
	return ans
}

// func main() {
// 	i := countNumbersWithUniqueDigits(3)
// 	fmt.Printf("i: %v\n", i)
// }
