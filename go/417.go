package main

import "fmt"

var dirs = []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func pacificAtlantic(heights [][]int) (ans [][]int) {

	w, h := len(heights[0]), len(heights)

	var dfs func(int, int, [][]bool)
	dfs = func(x int, y int, result [][]bool) {
		if result[x][y] {
			return
		}
		result[x][y] = true
		for _, dir := range dirs {
			nx, ny := x+dir.x, y+dir.y
			// fmt.Printf("nx: %v\n", nx)
			// fmt.Printf("ny: %v\n", ny)
			if 0 <= nx && nx < h && 0 <= ny && ny < w && heights[nx][ny] >= heights[x][y] {
				dfs(nx, ny, result)
			}
		}
	}

	pResult := make([][]bool, h)
	aResult := make([][]bool, h)
	for i := range pResult {
		// fmt.Printf("i: %v\n", i)
		pResult[i] = make([]bool, w)
		aResult[i] = make([]bool, w)
	}

	// fmt.Printf("pResult: %v\n", pResult)
	// fmt.Printf("aResult: %v\n", aResult)

	for i := 0; i < h; i++ {
		dfs(i, 0, pResult)
		dfs(i, w-1, aResult)
	}
	for j := 0; j < w; j++ {
		dfs(h-1, j, aResult)
		dfs(0, j, pResult)
	}

	fmt.Printf("pResult: %v\n", pResult)
	fmt.Printf("aResult: %v\n", aResult)

	for x := 0; x < h; x++ {
		for y := 0; y < w; y++ {
			if pResult[x][y] && aResult[x][y] {
				ans = append(ans, []int{x, y})
			}
		}
	}
	return ans
}

func main() {
	heights := make([][]int, 0)
	// for i := range heights {
	heights = append(heights, []int{1, 2, 2, 3, 5})
	heights = append(heights, []int{3, 2, 3, 4, 4})
	heights = append(heights, []int{2, 4, 5, 3, 1})
	heights = append(heights, []int{6, 7, 1, 4, 5})
	heights = append(heights, []int{5, 1, 1, 2, 4})
	// }
	ans := pacificAtlantic(heights)
	fmt.Printf("ans: %v\n", ans)
}
