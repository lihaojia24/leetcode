package main

import "fmt"

func isAlienSorted(words []string, order string) bool {
	index := [26]int{}
	for i, ch := range order {
		index[ch-'a'] = i
	}
next:
	for i := 1; i < len(words); i++ {
		for j := 0; j < len(words[i]) && j < len(words[i-1]); j++ {
			pre, cur := index[words[i-1][j]-'a'], index[words[i][j]-'a']
			if pre > cur {
				return false
			}
			if cur > pre {
				continue next
			}
		}
		if len(words[i-1]) > len(words[i]) {
			return false
		}
	}
	return true
}

func main() {
	ans := "abcc" >= "abc"
	fmt.Printf("ans: %v\n", ans)
}
