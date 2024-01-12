package main

func minDeletionSize(strs []string) (ans int) {
	row := len(strs)
	col := len(strs[0])
	for c := 0; c < col; c++ {
		tmp := strs[0][c]
		for r := 1; r < row; r++ {
			if strs[r][c] >= tmp {
				tmp = strs[r][c]
			} else {
				ans++
				break
			}
		}
	}
	return
}

// func main() {
// 	strs := []string{"abc", "bce", "caa"}
// 	ans := minDeletionSize(strs)
// 	fmt.Printf("ans: %v\n", ans)
// }
