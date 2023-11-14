package main

import "math"

func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	G := make([][]int, n)
	for i := range G {
		G[i] = make([]int, n)
		for j := range G[i] {
			G[i][j] = math.MaxInt / 2
		}
	}
	for _, edge := range edges {
		x, y, w := edge[0], edge[1], edge[2]
		G[x][y] = w
		G[y][x] = w
	}
	for p := 0; p < n; p++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if i == j || i == p || j == p {
					continue
				}
				G[i][j] = min(G[i][j], G[i][p]+G[p][j])
			}
		}
	}
	ans := 0
	minCnt := n
	for i := 0; i < n; i++ {
		cnt := 0
		for j := 0; j < n; j++ {
			if G[i][j] <= distanceThreshold {
				cnt++
			}
		}
		if cnt <= minCnt {
			minCnt = cnt
			ans = i
		}
	}
	return ans
}

func main() {

}
