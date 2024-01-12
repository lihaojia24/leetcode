package main

import "strings"

func toGoatLatin(sentence string) string {
	vowels := map[byte]int{
		'a': 1,
		'e': 1,
		'i': 1,
		'o': 1,
		'u': 1,
		'A': 1,
		'E': 1,
		'I': 1,
		'O': 1,
		'U': 1,
	}
	ans := &strings.Builder{}
	n := len(sentence)
	cnt := 1
	for i := 0; i < n; {
		if cnt > 1 {
			ans.WriteByte(' ')
		}
		start := i
		for ; i < n && sentence[i] != ' '; i++ {
		}
		cnt++
		if _, ok := vowels[sentence[start]]; ok {
			ans.WriteString(sentence[start:i])
		} else {
			ans.WriteString(sentence[start+1 : i])
			ans.WriteByte(sentence[start])
		}
		ans.WriteByte('m')
		ans.WriteString(strings.Repeat("a", cnt))
		i++
	}
	return ans.String()
}
