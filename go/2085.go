package main

func countWords(words1 []string, words2 []string) int {
	m1 := make(map[string]int)
	m2 := make(map[string]int)
	for _, word := range words1 {
		v, ok := m1[word]
		if ok {
			m1[word] = v + 1
		} else {
			m1[word] = 1
		}
	}
	for _, word := range words2 {
		v, ok := m2[word]
		if ok {
			m2[word] = v + 1
		} else {
			m2[word] = 1
		}
	}
	res := 0
	for k, v := range m1 {
		if v == 1 && m2[k] == 1 {
			res++
		}
	}
	return res
}
