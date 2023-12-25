package main

func numOfBurgers(tomatoSlices int, cheeseSlices int) []int {
	if tomatoSlices%2 == 1 {
		return []int{}
	}
	if tomatoSlices < cheeseSlices*2 || tomatoSlices > cheeseSlices*4 {
		return []int{}
	}
	x := (tomatoSlices - 2*cheeseSlices) / 2
	return []int{x, cheeseSlices - x}
}
