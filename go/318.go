package main

func maxProduct(words []string) (ans int) {
	n := len(words)
	masks := make([]int, n)
	for i, word := range words {
		mask := 0
		for _, ch := range word {
			mask |= 1 << (ch - 'a')
		}
		masks[i] = mask
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if masks[i]&masks[j] == 0 {
				ans = max(len(words[i])*len(words[j]), ans)
			}
		}
	}
	return
}
