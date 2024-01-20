package main

func fillCups(amount []int) int {
	a, b, c := amount[0], amount[1], amount[2]
	if b > a {
		a, b = b, a
	}
	if c > a {
		a, c = c, a
	}
	if a > b+c {
		return a
	} else {
		return (a+b+c)/2 + (a+b+c)%2
	}
}
