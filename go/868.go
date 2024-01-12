package main

func binaryGap(n int) (ans int) {
	last := -1
	for i := 0; n > 0; i++ {
		if n&1 == 1 {
			if last != -1 {
				ans = max(ans, i-last)
			}
			last = i
		}
		n >>= 1
	}
	return
}
