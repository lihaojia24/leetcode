package main

func maximumNumberOfStringPairs(words []string) (res int) {
	m := map[int]int{}
	for _, word := range words {
		x := int(word[0])*100 + int(word[1])
		rx := int(word[1])*100 + int(word[0])
		res += m[rx]
		m[x]++
	}
	return res
}
