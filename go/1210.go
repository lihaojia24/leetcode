package main

type tuple struct{ x, y, z int }

var dirs = []tuple{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}

func minimumMoves(grid [][]int) int {
	n := len(grid)
	vis := make([][][2]bool, n)
	for i := range vis {
		vis[i] = make([][2]bool, n)
	}
	vis[0][0][0] = true
	q := []tuple{{0, 0, 0}}
	for step := 1; len(q) > 0; step++ {
		tmp := q
		q = nil
		for _, t := range tmp {
			for _, d := range dirs {
				x, y, z := t.x+d.x, t.y+d.y, t.z^d.z
				hx, hy := x+z, y+(z^1)
				if hx < n && hy < n && !vis[x][y][z] && grid[x][y] == 0 && grid[hx][hy] == 0 && (d.z == 0 || grid[x+1][y+1] == 0) {

					if x == n-1 && y == n-2 {
						return step
					}
					vis[x][y][z] = true
					q = append(q, tuple{x, y, z})
				}
			}
		}
	}
	return -1
}
