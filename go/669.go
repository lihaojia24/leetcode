package main

import (
	"fmt"
	"sort"
)

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func fallingSquares(positions [][]int) (ans []int) {
	heightMap := map[int]int{0: 0}
	keys := []int{0}
	tMax := 0
	for _, pos := range positions {
		height, last := 0, 0
		sort.Slice(keys, func(i, j int) bool {
			return keys[i] < keys[j]
		})
		for _, key := range keys {
			val := heightMap[key]
			if key <= pos[0] {
				height = val
				last = val
			} else if key < pos[0]+pos[1] {
				height = max(height, val)
				last = val
			}
		}

		// for i := 0; i < pos[0]+pos[1]; i++ {
		// 	if val, ok := heightMap[i]; ok {
		// 		if i <= pos[0] {
		// 			height = val
		// 		} else {
		// 			height = max(height, val)
		// 		}
		// 		last = val
		// 	}
		// }
		height += pos[1]
		tMax = max(tMax, height)
		ans = append(ans, tMax)

		//left
		if _, ok := heightMap[pos[0]]; !ok {
			keys = append(keys, pos[0])
		}
		heightMap[pos[0]] = height
		// fmt.Printf("keys: %v\n", keys)

		// middle
		var delI []int
		// fmt.Printf("keys: %v\n", keys)
		// fmt.Printf("keysT: %v\n", keysT)
		for i, key := range keys {
			if key > pos[0] && key < pos[0]+pos[1] {
				delete(heightMap, key)
				delI = append(delI, i)
			}
		}
		for i, index := range delI {
			keys = append(keys[:index-i], keys[index-i+1:]...)
		}
		// keys = keysT
		// fmt.Printf("keys: %v\n", keys)
		// for i := pos[0] + 1; i < pos[0]+pos[1]; i++ {
		// 	if _, ok := heightMap[i]; ok {
		// 		delete(heightMap, i)
		// 	}
		// }

		//right

		if _, ok := heightMap[pos[0]+pos[1]]; !ok {
			heightMap[pos[0]+pos[1]] = last
			keys = append(keys, pos[0]+pos[1])
		}
		fmt.Printf("heightMap: %v\n", heightMap)
		fmt.Printf("keys: %v\n", keys)
	}
	return
}

func main() {

}
