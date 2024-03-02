package main

func reachableNodes(n int, edges [][]int, restricted []int) (ans int) {
	g := make([][]int, n)
	for _, edge := range edges {
		x, y := edge[0], edge[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}
	m := make([]bool, n)
	for _, rest := range restricted {
		m[rest] = true
	}
	var helper func(node, fa int)
	helper = func(node, fa int) {
		if m[node] {
			return
		}
		ans++
		for _, nxt := range g[node] {
			if nxt != fa {
				helper(nxt, node)
			}
		}
	}
	helper(0, -1)
	return
}
