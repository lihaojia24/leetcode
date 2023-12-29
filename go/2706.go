package main

func buyChoco(prices []int, money int) int {
	var a, b int
	if prices[0] < prices[1] {
		a, b = prices[0], prices[1]
	} else {
		a, b = prices[1], prices[0]
	}
	for i := 2; i < len(prices); i++ {
		if prices[i] < b {
			if prices[i] < a {
				a, b = prices[i], a
			} else {
				b = prices[i]
			}
		}
	}
	if a+b > money {
		return money
	}
	return money - a - b
}
