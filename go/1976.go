package main

func countPaths(n int, roads [][]int) int {
	g := make([][][2]int, n)
	for _, road := range roads {
		x, y, d := road[0], road[1], road[2]
		g[x] = append(g[x], [2]int{y, d})
		g[y] = append(g[y], [2]int{x, d})
	}
	counts := make([]int, n)
	dists := make([]int, n)
	dones := make([]bool, n)
	for i := range dists {
		dists[i] = -1
	}
	dists[0] = 0
	counts[0] = 1
	dones[0] = true
	minNode := 0
	for i := 0; i < n-1; i++ {
		for _, nxtNode := range g[minNode] {
			nxt, d := nxtNode[0], nxtNode[1]
			if dones[nxt] {
				continue
			}
			if dists[nxt] == -1 || d+dists[minNode] < dists[nxt] {
				counts[nxt] = counts[minNode]
				dists[nxt] = d + dists[minNode]
			} else if d+dists[minNode] == dists[nxt] {
				counts[nxt] = (counts[nxt] + counts[minNode]) % 1_000_000_007
			}
		}
		minNode = -1
		for j := 0; j < n; j++ {
			if !dones[j] && dists[j] != -1 && (minNode == -1 || dists[j] < dists[minNode]) {
				minNode = j
			}
		}
		dones[minNode] = true
		// fmt.Printf("minNode: %v\n", minNode)
		// fmt.Printf("dists: %v\n", dists)
		// fmt.Printf("counts: %v\n", counts)
	}

	return counts[n-1]
}
