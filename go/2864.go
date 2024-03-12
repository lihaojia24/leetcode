package main

import "strings"

func maximumOddBinaryNumber(s string) string {
	n := len(s)
	cnt := strings.Count(s, "1") - 1
	return strings.Repeat("1", cnt) + strings.Repeat("0", n-cnt-1) + "1"
}
