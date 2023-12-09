package main

func nextBeautifulNumber(n int) int {
	var check func(n int) bool
	check = func(n int) bool {
		m := make(map[int]int, 0)
		for n > 0 {
			x := n % 10
			n = n / 10
			m[x]++
		}
		for k, v := range m {
			if k != v {
				return false
			}
		}
		return true
	}

	for n++; n < 1224445; n++ {
		if check(n) {
			return n
		}
	}
	return -1
}
