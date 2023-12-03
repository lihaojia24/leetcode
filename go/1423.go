package main

func maxScore(cardPoints []int, k int) int {
	n := len(cardPoints)
	points := make([]int, k+1)
	left := 0
	right := 0
	for i := 0; i < k; i++ {
		left += cardPoints[i]
		right += cardPoints[n-1-i]
		points[i+1] += left
		points[k-1-i] += right
	}
	ans := 0
	for _, point := range points {
		if point > ans {
			ans = point
		}
	}
	return ans
}
