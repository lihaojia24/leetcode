package main

func numberOfBoomerangs(points [][]int) int {
	n := len(points)
	ms := make([]map[int]int, n)
	for i := range ms {
		ms[i] = map[int]int{}
	}
	for i := range points {
		for j := i + 1; j < n; j++ {
			d := (points[i][0]-points[j][0])*(points[i][0]-points[j][0]) + (points[i][1]-points[j][1])*(points[i][1]-points[j][1])
			ms[i][d]++
			ms[j][d]++
		}
	}
	ans := 0
	for i := range points {
		for _, v := range ms[i] {
			ans += v * (v - 1)
		}
	}
	return ans
}
