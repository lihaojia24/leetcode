package main

import "fmt"

func alphabetBoardPath(target string) string {
	ans := []byte{}
	x, y := 0, 0
	num, row, col := 0, 0, 0
	for _, ch := range target {
		num = int(ch - 'a')
		row, col = num/5, num%5
		for row < y {
			y--
			ans = append(ans, 'U')
		}
		for col > x {
			x++
			ans = append(ans, 'R')
		}
		for col < x {
			x--
			ans = append(ans, 'L')
		}
		for row > y {
			y++
			ans = append(ans, 'D')
		}
		ans = append(ans, '!')
	}
	return string(ans)
}

func main() {
	target := "code"
	fmt.Printf("alphabetBoardPath(target): %v\n", alphabetBoardPath(target))
}
