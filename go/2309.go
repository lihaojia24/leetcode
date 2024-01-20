package main

import (
	"unicode"
)

// func main() {
// 	s := "lEeTcOdE"
// 	fmt.Printf("greatestLetter(s): %v\n", greatestLetter(s))
// }

func greatestLetter(s string) string {
	chs := [26]int{}
	for _, ch := range s {
		if unicode.IsLower(ch) {
			chs[ch-'a'] |= 1
		} else {
			chs[ch-'A'] |= 2
		}
	}
	for i := 25; i > -1; i-- {
		if chs[i] == 3 {
			return string(i + 'A')
		}
	}
	return ""
}
