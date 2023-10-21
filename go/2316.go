package main

func countPairs(n int, edges [][]int) (ans int64) {
	g := make([][]int, n)
	for _, edge := range edges {
		x, y := edge[0], edge[1]
		g[x] = append(g[x], y)
		g[y] = append(g[y], x)
	}
	v := make([]bool, n)
	var dfs func(int) int
	dfs = func(i int) (ans int) {
		q := make([]int, 1)
		q[0] = i
		for len(q) > 0 {
			x := q[len(q)-1]
			q = q[:len(q)-1]
			if !v[x] {
				ans++
				v[x] = true
				for _, y := range g[x] {
					q = append(q, y)
				}
			}
		}
		return
	}
	total := 0
	for i := 0; i < n; i++ {
		s := dfs(i)
		ans += int64(total * s)
		total += s
	}
	return ans
}

func main() {

}
