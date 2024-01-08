package main

import "fmt"

func minExtraChar(s string, dictionary []string) int {
	n := len(s)
	res := make([]int, n)
	for i := range s {
		res[i] = 1
		if i > 0 {
			res[i] = res[i-1] + 1
		}
		for _, word := range dictionary {
			if i >= len(word)-1 && s[i-len(word)+1:i+1] == word {
				if i-len(word) < 0 {
					res[i] = 0
				} else {
					res[i] = min(res[i], res[i-len(word)])
				}
			}
		}
	}
	fmt.Printf("res: %v\n", res)
	return res[len(res)-1]
}
