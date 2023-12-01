package main

import "sort"

func closeStrings(word1 string, word2 string) bool {
	countA := make([]int, 26)
	countB := make([]int, 26)
	for _, word := range word1 {
		countA[word-'a']++
	}
	for _, word := range word2 {
		countB[word-'a']++
	}
	for i := range countA {
		if countA[i] > 0 && countB[i] == 0 {
			return false
		}
		if countB[i] > 0 && countA[i] == 0 {
			return false
		}
	}
	sort.Ints(countA)
	sort.Ints(countB)
	for i := range countA {
		if countA[i] != countB[i] {
			return false
		}
	}
	return true
}

func main() {

}
