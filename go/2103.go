package main

func countPoints(rings string) int {
	n := len(rings)
	res := make([]int, 10)
	for i := 0; i < n; i += 2 {
		pos := rings[i+1] - '0'
		if rings[i] == 'R' {
			res[pos] |= 1
		}
		if rings[i] == 'G' {
			res[pos] |= 1 << 1
		}
		if rings[i] == 'B' {
			res[pos] |= 1 << 2
		}
	}
	ans := 0
	for _, num := range res {
		if num == 7 {
			ans++
		}
	}
	return ans
}
