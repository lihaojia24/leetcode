package main

func minimumFuelCost(roads [][]int, seats int) (ans int64) {
	n := len(roads) + 1
	g := make([][]int, n)
	for _, road := range roads {
		x, y := road[0], road[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}
	var dfs func(root, fa int) int
	dfs = func(root, fa int) int {
		size := 1
		for _, x := range g[root] {
			if x != fa {
				size += dfs(x, root)
			}
		}
		ans += int64((size-1)/seats + 1)
		return size
	}
	for _, x := range g[0] {
		ans += int64(dfs(x, 0))
	}
	return
}
