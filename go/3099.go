package main

func sumOfTheDigitsOfHarshadNumber(x int) int {
	s := 0
	o := x
	for x > 0 {
		s += x % 10
		x /= 10
	}
	if o%s == 0 {
		return s
	}
	return -1
}
