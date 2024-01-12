package main

func findAndReplacePattern(words []string, pattern string) (ans []string) {
next:
	for _, word := range words {
		m := map[rune]byte{}
		u := map[byte]int{}
		for i, ch := range word {
			p := pattern[i]
			if m[ch] == 0 {
				if u[p] == 0 {
					m[ch] = p
					u[p] = 1
				} else {
					continue next
				}
			} else if m[ch] != p {
				continue next
			}
		}
		ans = append(ans, word)
	}
	return
}

// func main() {
// 	words := []string{"abc", "deq", "mee", "aqq", "dkd", "ccc"}
// 	pattern := "abb"
// 	fmt.Printf("findAndReplacePattern(words, pattern): %v\n", findAndReplacePattern(words, pattern))
// }
