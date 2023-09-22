package main

import "fmt"

func distMoney(money int, children int) (ans int) {
	if money > 8*children {
		return children - 1
	}
	if money == 8*children {
		return children
	}
	if money < children {
		return -1
	}
	if money == 4 && children == 1 {
		return -1
	}
	money -= children
	ans = money / 7
	if (ans == children-1) && (money%7 == 3) {
		ans--
	}
	return
}

func main() {
	fmt.Printf("distMoney(20, 3): %v\n", distMoney(20, 3))
}
