package main

func distanceTraveled(mainTank int, additionalTank int) int {
	res := 0
	for mainTank >= 5 && additionalTank > 0 {
		t := mainTank / 5
		mainTank %= 5
		res += 5 * t
		t = min(additionalTank, t)
		additionalTank -= t
		mainTank += t
	}
	res += mainTank
	return 10 * res
}
