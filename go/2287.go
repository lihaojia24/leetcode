package main

import "fmt"

// func main() {
// 	s := "ilovecodingonleetcode"
// 	target := "code"
// 	fmt.Printf("rearrangeCharacters(s, target): %v\n", rearrangeCharacters(s, target))
// }

func rearrangeCharacters(s string, target string) int {
	m := map[rune]int{}
	m2 := map[rune]int{}
	for _, ch := range target {
		m[ch] += 1
	}

	for _, ch := range s {
		if _, ok := m[ch]; ok {
			m2[ch] += 1
		}
	}
	fmt.Printf("m: %v\n", m)
	fmt.Printf("m2: %v\n", m2)
	ans := -1
	for k, v := range m {
		if ans != -1 {
			if m2[k]/v < ans {
				ans = m2[k] / v
			}
		} else {
			ans = m2[k] / v
		}
	}
	return ans
}
