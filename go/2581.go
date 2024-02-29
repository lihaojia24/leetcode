package main

type pair struct {
	x, y int
}

func rootCount(edges [][]int, guesses [][]int, k int) (ans int) {
	g := make([][]int, len(edges)+1)
	for _, e := range edges {
		x, y := e[0], e[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}
	guess_m := make(map[pair]bool, len(guesses))
	for _, guess := range guesses {
		guess_m[pair{guess[0], guess[1]}] = true
	}
	cnt0 := 0
	var dfs func(x, fa int)
	dfs = func(x, fa int) {
		if guess_m[pair{fa, x}] {
			cnt0++
		}
		for _, y := range g[x] {
			if y != fa {
				dfs(y, x)
			}
		}
	}
	var reroot func(x, fa, cnt int)
	reroot = func(x, fa, cnt int) {
		if guess_m[pair{fa, x}] {
			cnt--
		}
		if guess_m[pair{x, fa}] {
			cnt++
		}
		if cnt >= k {
			ans++
		}
		for _, y := range g[x] {
			if y != fa {
				reroot(y, x, cnt)
			}
		}
	}
	dfs(0, -1)
	reroot(0, -1, cnt0)
	return
}
