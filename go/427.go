package main

type Node struct {
	Val         bool
	IsLeaf      bool
	TopLeft     *Node
	TopRight    *Node
	BottomLeft  *Node
	BottomRight *Node
}

func construct(grid [][]int) *Node {
	n := len(grid)
	pre := make([][]int, n+1)
	pre[0] = make([]int, n+1)
	for i, row := range grid {
		pre[i+1] = make([]int, n+1)
		for j, v := range row {
			pre[i+1][j+1] = pre[i+1][j] + pre[i][j+1] - pre[i][j] + v
		}
	}
	var dfs func(r0, r1, c0, c1 int) *Node
	dfs = func(r0, r1, c0, c1 int) *Node {
		total := pre[r1][c1] - pre[r1][c0] - pre[r0][c1] + pre[r0][c0]
		if total != 0 && total != (r1-r0)*(c1-c0) {
			rMid, cMid := (r0+r1)/2, (c0+c1)/2
			return &Node{
				Val:         true,
				IsLeaf:      false,
				TopLeft:     dfs(r0, rMid, c0, cMid),
				TopRight:    dfs(r0, rMid, cMid, c1),
				BottomLeft:  dfs(rMid, r1, c0, cMid),
				BottomRight: dfs(rMid, r1, cMid, c1),
			}
		} else {
			return
		}
		// for r := r0; r < r1; r++ {
		// 	for c := c0; c < c1; c++ {
		// 		if grid[r][c] != grid[r0][c0] {
		// 			// not leaf
		// 			rMid, cMid := (r0+r1)/2, (c0+c1)/2
		// 			return &Node{
		// 				Val:         true,
		// 				IsLeaf:      false,
		// 				TopLeft:     dfs(r0, rMid, c0, cMid),
		// 				TopRight:    dfs(r0, rMid, cMid, c1),
		// 				BottomLeft:  dfs(rMid, r1, c0, cMid),
		// 				BottomRight: dfs(rMid, r1, cMid, c1),
		// 			}
		// 		}
		// 	}
		// }
		return &Node{
			Val:    grid[r0][c0] == 1,
			IsLeaf: true,
		}
	}
	return dfs(0, len(grid), 0, len(grid))
}

func main() {

}
