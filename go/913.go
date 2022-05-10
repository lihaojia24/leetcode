package main

func catMouseGame(graph [][]int) int {
	n := len(graph)
	// init dp
	// step, mouse, cat
	dp := make([][][]int, 2*n*n)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, n)
			for k := range dp[i][j] {
				dp[i][j][k] = -1
			}
		}
	}
	// def dfs
	// step, mouse, cat
	// 1-mouse, 2-cat win
	var dfs func(s, m, c int) int
	dfs = func(s, m, c int) (ans int) {
		ans = dp[s][m][c]
		if m == 0 {
			ans = 1
		} else if m == c {
			ans = 2
		} else if s >= 2*n*n {
			ans = 0
		} else if ans == -1 {
			// unknow situation
			// mouse step
			if s%2 == 0 {
				win, even := false, false
				for _, mNex := range graph[m] {
					nxt := dfs(s+1, mNex, c)
					if nxt == 1 {
						win = true
						break
					} else if nxt == 0 {
						even = true
					}
				}
				if win {
					ans = 1
				} else if even {
					ans = 0
				} else {
					ans = 2
				}
			} else { // cat step
				win, even := false, false
				for _, cNex := range graph[c] {
					if cNex == 0 {
						continue
					}
					nxt := dfs(s+1, m, cNex)
					if nxt == 2 {
						win = true
						break
					} else if nxt == 0 {
						even = true
					}
				}
				if win {
					ans = 2
				} else if even {
					ans = 0
				} else {
					ans = 1
				}
			}
		}
		dp[s][m][c] = ans
		return
	}

	return dfs(0, 1, 2)
}

func main() {

}
