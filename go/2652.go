package main

func sumOfMultiples(n int) int {
	var s func(int) int
	s = func(m int) int {
		return n / m * (n/m + 1) / 2 * m
	}
	return s(3) + s(5) + s(7) + s(105) - s(15) - s(21) - s(35)
}
