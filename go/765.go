package main

import "fmt"

func minSwapsCouples(row []int) (ans int) {
	n := len(row)
	pos := make([]int, n)
	for index, p := range row {
		pos[p] = index
	}
	for i := 0; i < n; i += 2 {
		if row[i]^row[i+1] != 1 {
			ans++
			row[pos[row[i]^1]] = row[i+1]
			pos[row[i+1]] = pos[row[i]^1]
		}
		fmt.Printf("row: %v\n", row)
	}
	return
}

// func main() {
// 	row := []int{0, 2, 4, 6, 7, 1, 3, 5}
// 	minSwapsCouples(row)
// }
