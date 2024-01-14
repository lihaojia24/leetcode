package main

func balancedString(s string) int {
	l := len(s) / 4
	m := map[byte]int{}
	var check func(map[byte]int) bool
	check = func(m map[byte]int) bool {
		for _, v := range m {
			if v > l {
				return false
			}
		}
		return true
	}
	var min func(a, b int) int
	min = func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	for _, ch := range s {
		m[byte(ch)]++
	}
	if check(m) {
		return 0
	}
	res := len(s)
	j := 0
	for i := 0; i < len(s); i++ {
		for j < len(s) && !check(m) {
			m[s[j]]--
			j++
		}
		if !check(m) {
			return res
		}
		res = min(res, j-i)
		m[s[i]]++
	}
	return res
}

// func main() {
// 	s := "WQWRQQQW"
// 	fmt.Printf("balancedString(s): %v\n", balancedString(s))
// }
