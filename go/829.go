package main

func consecutiveNumbersSum(n int) int {
	// (s + s + k - 1) * k = 2 * n
	// (2s + k - 1) * k = 2n
	n2 := 2 * n
	ans := 0
	for k := 1; k*k <= n2; k++ {
		if n2%k == 0 {
			a := n2/k - k + 1
			if a > 0 && a%2 == 0 {
				ans++
			}
		}
	}
	return ans
}

// func main() {
// 	fmt.Printf("consecutiveNumbersSum(5): %v\n", consecutiveNumbersSum(15))
// }
