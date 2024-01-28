package main

func canMeasureWater(j1 int, j2 int, cap int) bool {
	if j1+j2 < cap {
		return false
	}
	if j1 == 0 || j2 == 0 {
		return cap == 0 || cap == j1+j2
	}
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	return cap%gcd(j1, j2) == 0
}
