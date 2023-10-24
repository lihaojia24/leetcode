package main

import "strconv"

var m [1001]int

func init() {
	for i := 1; i < 1001; i++ {
		s := strconv.Itoa(i * i)
		n := len(s)
		var dfs func(p int, total int) bool
		dfs = func(p, total int) bool {
			if p == n {
				return total == i
			}
			x := 0
			for j := p; j < n; j++ {
				x = x*10 + int(s[j]-'0')
				if dfs(j+1, total+x) {
					return true
				}
			}
			return false
		}
		m[i] = m[i-1]
		if dfs(0, 0) {
			m[i] += i * i
		}
	}
}

func punishmentNumber(n int) int {
	return m[n]
}

func main() {

}
