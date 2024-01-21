package main

func countDigits(num int) (ans int) {
	t := num
	for t > 0 {
		if num%(t%10) == 0 {
			ans++
		}
		t /= 10
	}
	return
}
