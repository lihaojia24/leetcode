package main

func findPeakGrid(mat [][]int) []int {
	l, r := 0, len(mat)-1
	for l < r {
		mid := l + (r-l)/2
		idx := indexOfMax(mat[mid])
		if mat[mid+1][idx] > mat[mid][idx] {
			l = mid + 1
		} else {
			r = mid
		}
	}
	return []int{l, indexOfMax(mat[l])}
}

func indexOfMax(a []int) (idx int) {
	for i, x := range a {
		if x > a[idx] {
			idx = i
		}
	}
	return
}
