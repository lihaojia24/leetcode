package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func minFlipsMonoIncr(s string) int {
	num0, num1 := 0, 0
	for _, ch := range s {
		if ch == '1' {
			num0, num1 = num0+1, min(num0, num1)
		} else {
			num1 = min(num0+1, num1+1)
		}
		fmt.Println(num0, num1)
	}
	return min(num0, num1)
}

func main() {
	s := "00011000"
	fmt.Printf("minFlipsMonoIncr(s): %v\n", minFlipsMonoIncr(s))
}
