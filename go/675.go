package main

import (
	"fmt"
	"sort"
)

var dir4 = []struct{ r, c int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func cutOffTree(forest [][]int) int {
	rowLen, colLen := len(forest), len(forest[0])
	type tree struct{ h, r, c int }
	trees := []tree{}
	for row := 0; row < rowLen; row++ {
		for col := 0; col < colLen; col++ {
			if forest[row][col] > 1 {
				trees = append(trees, tree{forest[row][col], row, col})
			}
		}
	}
	sort.Slice(trees, func(i, j int) bool {
		return trees[i].h <= trees[j].h
	})

	var dfs func(startRow, startCol, endRow, endCol int) int
	dfs = func(startRow, startCol, endRow, endCol int) int {
		visited := make([][]bool, rowLen)
		for i := range visited {
			visited[i] = make([]bool, colLen)
		}
		visited[startRow][startCol] = true
		type step struct{ s, r, c int }
		q := []step{{0, startRow, startCol}}
		for len(q) > 0 {
			cur := q[0]
			q = q[1:]
			if cur.r == endRow && cur.c == endCol {
				return cur.s
			}
			for _, d := range dir4 {
				nr, nc := cur.r+d.r, cur.c+d.c
				if 0 <= nr && nr < rowLen && 0 <= nc && nc < colLen && !visited[nr][nc] && forest[nr][nc] > 0 {
					visited[nr][nc] = true
					q = append(q, step{cur.s + 1, nr, nc})
				}
			}
		}
		return -1
	}

	preR, preC, ans := 0, 0, 0
	for _, tree := range trees {
		fmt.Printf("preR: %v\n", preR)
		fmt.Printf("preC: %v\n", preC)
		fmt.Printf("tree.r: %v\n", tree.r)
		fmt.Printf("tree.c: %v\n", tree.c)

		d := dfs(preR, preC, tree.r, tree.c)
		fmt.Printf("d: %v\n", d)
		if d < 0 {
			return -1
		} else {
			ans += d
		}
		preR, preC = tree.r, tree.c
	}
	return ans
}

func main() {

}
