package main

import "math"

func triangleArea(x1, y1, x2, y2, x3, y3 int) float64 {
	return math.Abs(float64((y1-y2)*x3+(y2-y3)*x1+(y3-y1)*x2)) / 2
}

func maxf(s1, s2 float64) float64 {
	if s1 > s2 {
		return s1
	} else {
		return s2
	}
}

func largestTriangleArea(points [][]int) (ans float64) {
	for i, p1 := range points {
		for j, p2 := range points[:i] {
			for _, p3 := range points[:j] {
				ans = maxf(ans, triangleArea(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]))
			}
		}
	}
	return
}

// func main() {

// }
