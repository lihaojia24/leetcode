package main

func canIWin(maxChoosableInteger int, desiredTotal int) bool {
	// 0: not visisted, 1: win, 2: loss
	visited := make([]int8, (1<<maxChoosableInteger)+1)
	var dfs func(state int, sum int) bool
	dfs = func(state, sum int) bool {
		if visited[state] == 1 {
			return true
		}
		if visited[state] == 2 {
			return false
		}
		for i := maxChoosableInteger - 1; i >= 0; i-- {
			if (1<<i)&state != 0 {
				continue
			}
			if sum+i+1 >= desiredTotal {
				visited[state] = 1
				return true
			}
			if !dfs(state|(1<<i), sum+i+1) {
				visited[state] = 1
				return true
			}
		}
		visited[state] = 2
		return false
	}
	if maxChoosableInteger >= desiredTotal {
		return true
	}
	if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal {
		return false
	}
	return dfs(0, 0)
}

// func main() {

// }
