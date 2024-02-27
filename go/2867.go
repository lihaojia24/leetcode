package main

const mx int = 1e5 + 1

var np = [mx]bool{1: true}

func init() {
	for i := 2; i*i < mx; i++ {
		if !np[i] {
			for j := i * i; j < mx; j += i {
				np[j] = true
			}
		}
	}
}

func countPaths(n int, edges [][]int) (ans int64) {
	g := make([][]int, n+1)
	for _, e := range edges {
		x, y := e[0], e[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}
	// fmt.Printf("g: %v\n", g)
	size := make([]int, n+1)
	var countSize func(x int)
	countSize = func(x int) {
		if !np[x] {
			return
		}
		caled := make([]bool, n+1)
		caled[x] = true
		nodes := []int{x}
		st := []int{x}
		for len(st) > 0 {
			node := st[len(st)-1]
			st = st[:len(st)-1]
			for _, other := range g[node] {
				// fmt.Printf("other: %v\n", other)
				if np[other] && !caled[other] {
					nodes = append(nodes, other)
					st = append(st, other)
					caled[other] = true
				}
			}
		}
		lnodes := len(nodes)
		// fmt.Printf("nodes: %v\n", nodes)
		for _, node := range nodes {
			size[node] = lnodes
		}
	}
	for x := 1; x <= n; x++ {
		if np[x] {
			continue
		}
		sum := 0
		for _, other := range g[x] {
			if size[other] == 0 {
				countSize(other)
			}
			ans += int64(sum) * int64(size[other])
			sum += size[other]
		}
		ans += int64(sum)
	}
	// fmt.Printf("size: %v\n", size)
	return
}
