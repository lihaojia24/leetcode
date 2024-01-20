package main

import "strings"

func splitWordsBySeparator(words []string, separator byte) (res []string) {
	for _, word := range words {
		sps := strings.Split(word, string([]byte{separator}))
		for _, sp := range sps {
			if len(sp) > 0 {
				res = append(res, sp)
			}
		}
	}
	return
}
