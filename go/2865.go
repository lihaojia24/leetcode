package main

func maximumSumOfHeights(maxHeights []int) int64 {
	n := len(maxHeights)
	// from left
	max_from_left := make([]int, n)
	sum_from_left := make([]int, n)
	s := 0
	for i, maxHeight := range maxHeights {
		preIndex := i - 1
		for preIndex >= 0 && max_from_left[preIndex] > maxHeight {
			s -= max_from_left[preIndex]
			s += maxHeight
			max_from_left[preIndex] = maxHeight
			preIndex--
		}
		s += maxHeight
		max_from_left[i] = maxHeight
		sum_from_left[i] = s
	}
	// from right
	max_from_right := make([]int, n)
	sum_from_right := make([]int, n)
	s = 0
	// maxHeightsReverse := make([]int, 0)
	// for i, maxHeight := range maxHeights {
	// 	maxHeightsReverse[n-i-1] = maxHeight
	// }
	for i := range maxHeights {
		index := n - i - 1
		maxHeight := maxHeights[index]
		preIndex := index + 1
		for preIndex < n && max_from_right[preIndex] > maxHeight {
			s -= max_from_right[preIndex]
			s += maxHeight
			max_from_right[preIndex] = maxHeight
			preIndex++
		}
		s += maxHeight
		max_from_right[index] = maxHeight
		sum_from_right[index] = s
	}
	// output
	// fmt.Printf("max_from_left: %v\n", max_from_left)
	// fmt.Printf("max_from_right: %v\n", max_from_right)
	res := 0
	for i := range max_from_right {
		res = max(res, sum_from_left[i]+sum_from_right[i]-maxHeights[i])
	}
	return int64(res)
}

// func main() {
// 	mh := []int{5, 3, 4, 1, 1}
// 	maximumSumOfHeights(mh)
// }
