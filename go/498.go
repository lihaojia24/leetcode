package main

func findDiagonalOrder(mat [][]int) (ans []int) {
	maxX, maxY := len(mat[0]), len(mat)
	startX, startY, flag := 0, 0, true
	for startX < maxX && startY < maxY {
		tX, tY := startX, startY
		tq := []int{}
		for 0 <= tX && tX < maxX && 0 <= tY && tY < maxY {
			tq = append(tq, mat[tX][tY])
			tX++
			tY--
		}
		if flag {
			ans = append(ans, tq...)
		} else {
			for i := 1; i <= len(tq); i++ {
				ans = append(ans, tq[len(tq)-i])
			}
		}
		if startY < maxY {
			startY++
		} else {
			startX++
		}
		flag = !flag
	}
	return
}

func main() {

}
