package main

import "math/bits"

func maximumRows(matrix [][]int, numSelect int) int {
	m, n := len(matrix), len(matrix[0])
	masks := make([]int, m)
	for i, row := range matrix {
		for j, x := range row {
			masks[i] |= x << j
		}
	}
	ans := 0
	for subset := 0; subset < 1<<n; subset++ {
		if bits.OnesCount(uint(subset)) == numSelect {
			covered_rows := 0
			for _, mask := range masks {
				if subset&mask == mask {
					covered_rows++
				}
			}
			ans = max(covered_rows, ans)
		}
	}
	return ans
}
