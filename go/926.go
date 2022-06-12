package main

import "fmt"

func minFlipsMonoIncr(s string) int {
	num, flag := 0, 0
	for _, ch := range s {
		if ch == '1' {
			flag = 1
		} else {
			if flag == 1 {
				num++
			}
		}
	}
	return num
}

func main() {
	s := "00011000"
	fmt.Printf("minFlipsMonoIncr(s): %v\n", minFlipsMonoIncr(s))
}
