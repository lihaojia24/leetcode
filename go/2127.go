package main

func maximumInvitations(favorite []int) int {
	n := len(favorite)
	deg := make([]int, n)
	maxDepth := make([]int, n)
	for _, f := range favorite {
		deg[f]++
	}
	q := []int{}
	for i, d := range deg {
		if d == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		nxt := favorite[node]
		maxDepth[nxt] = maxDepth[node] + 1
		deg[nxt]--
		if deg[nxt] == 0 {
			q = append(q, nxt)
		}
	}
	maxRingSize := 0
	maxLineSize := 0
	for i, d := range deg {
		if d != 0 {
			deg[i] = 0
			ringSize := 1
			x := favorite[i]
			for x != i {
				ringSize++
				deg[x] = 0
				x = favorite[x]
			}
			if ringSize == 2 {
				maxLineSize += maxDepth[i] + maxDepth[favorite[i]] + 2
			} else {
				maxRingSize = max(maxRingSize, ringSize)
			}
		}
	}
	return max(maxLineSize, maxRingSize)
}
