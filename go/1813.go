package main

import (
	"fmt"
	"strings"
)

func main() {
	sentence1 := "if of this"
	sentence2 := "if this"
	fmt.Printf("areSentencesSimilar(sentence1, sentence2): %v\n", areSentencesSimilar(sentence1, sentence2))
}

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	chs1 := strings.Split(sentence1, " ")
	chs2 := strings.Split(sentence2, " ")
	m := len(chs1)
	if len(chs1) > len(chs2) {
		m = len(chs2)
	}
	left1, right1 := 0, len(chs1)-1
	left2, right2 := 0, len(chs2)-1
	same := 0
	for left1 < right1+1 && left2 < right2+1 {
		if chs1[left1] != chs2[left2] {
			break
		}
		left1++
		left2++
		same++
	}
	for left1-1 < right1 && left2-1 < right2 {
		if chs1[right1] != chs2[right2] {
			break
		}
		right1--
		right2--
		same++
	}
	fmt.Printf("same: %v\n", same)
	if same == m {
		return true
	}
	return false
}
