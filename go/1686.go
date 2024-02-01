package main

import (
	"fmt"
	"sort"
)

func stoneGameVI(aliceValues []int, bobValues []int) int {
	n := len(aliceValues)
	resValues := make([][3]int, n)
	for i := 0; i < n; i++ {
		resValues[i] = [3]int{aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]}
	}
	sort.Slice(resValues, func(i, j int) bool {
		return resValues[i][0] > resValues[j][0]
	})
	resa := 0
	resb := 0
	for i := 0; i < n; i++ {
		if i%2 == 0 {
			resa += resValues[i][1]
		} else {
			resb += resValues[i][2]
		}
	}
	fmt.Printf("res: %v, %v\n", resa, resb)
	if resa > resb {
		return 1
	}
	if resa < resb {
		return -1
	}
	return 0
}

func main() {
	a := []int{1, 3}
	b := []int{2, 1}
	stoneGameVI(a, b)
}
