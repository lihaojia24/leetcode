package main

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func minCostToMoveChips(position []int) int {
	oddNum := 0
	evenNum := 0
	for _, v := range position {
		if v%2 == 1 {
			oddNum++
		} else {
			evenNum++
		}
	}
	return min(oddNum, evenNum)
}

func main() {

}
