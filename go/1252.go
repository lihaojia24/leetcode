package main

func oddCells(m int, n int, indices [][]int) int {
	ml := make([]int, m)
	nl := make([]int, n)
	for _, pos := range indices {
		ml[pos[0]]++
		nl[pos[1]]++
	}
	oddm, oddn := 0, 0
	for _, v := range ml {
		if v%2 == 1 {
			oddm++
		}
	}
	for _, v := range nl {
		if v%2 == 1 {
			oddn++
		}
	}
	return oddm*(n-oddn) + oddn*(m-oddm)
}

func main() {

}
