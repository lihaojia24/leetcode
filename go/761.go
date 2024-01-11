package main

import (
	"sort"
	"strings"
)

func makeLargestSpecial(s string) string {
	if len(s) < 3 {
		return s
	}
	ss := sort.StringSlice{}
	start, count := 0, 0
	for i, ch := range s {
		if ch == '1' {
			count++
		} else if count--; count == 0 {
			ss = append(ss, "1"+makeLargestSpecial(s[start+1:i])+"0")
			start = i + 1
		}
	}
	sort.Sort(sort.Reverse(ss))
	return strings.Join(ss, "")
}
