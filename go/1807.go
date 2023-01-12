package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "(name)is(age)yearsold"
	knowledge := [][]string{{"name", "bob"}, {"age", "two"}}
	fmt.Printf("evaluate(s, knowledge): %v\n", evaluate(s, knowledge))
}

func evaluate(s string, knowledge [][]string) string {
	dict := map[string]string{}
	for _, k := range knowledge {
		dict[k[0]] = k[1]
	}
	ans := &strings.Builder{}
	start := -1
	for i, ch := range s {
		if ch == '(' {
			start = i
		} else if ch == ')' {
			if v, ok := dict[s[start+1:i]]; ok {
				ans.WriteString(v)
			} else {
				ans.WriteByte('?')
			}
			start = -1
		} else {
			if start == -1 {
				ans.WriteRune(ch)
			}
		}
	}
	return ans.String()
}
