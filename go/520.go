package main

import "unicode"

func detectCapitalUse(word string) bool {
	cnt := 0
	for _, ch := range word {
		if unicode.IsUpper(ch) {
			cnt++
		}
	}
	return cnt == 0 || cnt == len(word) || cnt == 1 && unicode.IsUpper(rune(word[0]))
}
