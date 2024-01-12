package main

func numPrimeArrangements(n int) int {
	const MOD = 1e9 + 7
	ans := 1
	cnt1 := 1 // 合数
	cnt2 := 0 // 质数
	isComp := make([]bool, n+1)
	for i := 2; i < n+1; i++ {
		if isComp[i] {
			//合数
			cnt1++
			ans *= cnt1
			ans %= MOD
		} else {
			//质数
			cnt2++
			ans *= cnt2
			ans %= MOD
			//添加合数
			for j := i; j*i < n+1; j++ {
				isComp[j*i] = true
			}
		}
	}
	return ans
}

// func main() {
// 	n := 2
// 	fmt.Printf("numPrimeArrangements(n): %v\n", numPrimeArrangements(n))
// }
