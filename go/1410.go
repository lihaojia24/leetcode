package main

import (
	"strings"
)

func entityParser(text string) string {
	m := map[string]string{
		"&quot;":  "\"",
		"&apos;":  "'",
		"&gt;":    ">",
		"&lt;":    "<",
		"&frasl;": "/",
		"&amp;":   "&",
	}
	res := []string{}
	i := 0
	n := len(text)
	for i < n {
		isEntity := false
		if text[i] == '&' {
			for k, v := range m {
				if i+len(k)-1 < n && text[i:i+len(k)] == k {
					res = append(res, v)
					isEntity = true
					i += len(k) - 1
					break
				}
			}
		}
		if !isEntity {
			res = append(res, text[i:i+1])
		}
		i++
	}
	return strings.Join(res, "")
}

// func main() {
// 	s := "&amp; is an HTML entity but &ambassador; is not."
// 	fmt.Printf("entityParser(s): %v\n", entityParser(s))
// }
