package main

const MOD = 1_000_000_007

func minNonZeroProduct(p int) int {
	k := 1<<p - 1
	return k * my_pow(k-1, p-1) % MOD
}

func my_pow(x, p int) int {
	res := 1
	for x %= MOD; p > 0; p-- {
		res = (res * x) % MOD
		x = (x * x) % MOD
	}
	return res
}
