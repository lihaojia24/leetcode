package main

import "strings"

func capitalizeTitle(title string) string {
	words := strings.Fields(title)
	for i, word := range words {
		words[i] = strings.ToLower(word)
		if len(word) > 2 {
			words[i] = strings.Title(words[i])
		}
	}
	return strings.Join(words, " ")
}
