package main

import "fmt"

func findRotateSteps(ring string, key string) int {
	MAX_INT := 100_000_000_000
	N := len(ring)
	ch2pos := map[rune][]int{}
	for pos, ch := range ring {
		ch2pos[ch] = append(ch2pos[ch], pos)
	}
	findNext := func(pre_pos [][2]int, next_ch rune) (next_pos [][2]int) {
		for _, pos := range ch2pos[next_ch] {
			n_pos := [2]int{pos, MAX_INT}
			for _, p_pos := range pre_pos {
				dis := min((N+p_pos[0]-pos)%N, (N+pos-p_pos[0])%N)
				n_pos[1] = min(n_pos[1], p_pos[1]+dis+1)
			}
			next_pos = append(next_pos, n_pos)
		}
		return
	}
	pos := [][2]int{{0, 0}}
	for _, ch := range key {
		pos = findNext(pos, ch)
		fmt.Printf("pos: %v\n", pos)
	}
	res := pos[0][1]
	for _, p := range pos {
		res = min(res, p[1])
	}
	return res
}

func main() {
	ring := "godding"
	key := "gd"
	findRotateSteps(ring, key)
}
