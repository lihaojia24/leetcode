package main

func passThePillow(n int, time int) int {
	times := time / (n - 1)
	res := time % (n - 1)
	if times%2 == 0 {
		return res + 1
	}
	return n - res
}
