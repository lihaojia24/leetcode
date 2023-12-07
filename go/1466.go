package main

type P struct {
	n  int
	in bool
}

func minReorder(n int, connections [][]int) (ans int) {
	g := make([][]P, n)
	for _, conn := range connections {
		f, t := conn[0], conn[1]
		g[f] = append(g[f], P{t, false})
		g[t] = append(g[t], P{f, true})
	}
	var dfs func(root, fa int)
	dfs = func(root, fa int) {
		for _, p := range g[root] {
			if p.n != fa {
				if !p.in {
					ans++
				}
				dfs(p.n, root)
			}
		}
	}
	dfs(0, -1)
	return
}
