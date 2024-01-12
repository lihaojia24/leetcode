package main

import (
	"fmt"
	"unicode"
)

func mostCommonWord(paragraph string, banned []string) string {
	paragraphs := paragraph + string(' ')
	isBanded := map[string]bool{}
	for _, v := range banned {
		isBanded[v] = true
	}
	freq := map[string]int{}
	maxFreq := 0
	var word []byte
	ans := ""
	for _, ch := range paragraphs {
		if unicode.IsLetter(rune(ch)) {
			word = append(word, byte(unicode.ToLower(rune(ch))))
			fmt.Printf("word: %v\n", word)
		} else if word != nil {
			s := string(word)
			// fmt.Printf("s: %v\n", s)
			if !isBanded[s] {
				freq[s]++
				if freq[s] > maxFreq {
					ans = s
					maxFreq = freq[s]
				}
			}
			word = nil
		}
	}
	return ans
}

// func main() {
// 	paragraph := "Bob"
// 	banned := []string{}
// 	v := mostCommonWord(paragraph, banned)
// 	fmt.Printf("v: %v\n", v)

// }
