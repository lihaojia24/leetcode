package main

import (
	"fmt"
	"strings"
)

func printBin(num float64) string {
	ans := strings.Builder{}
	ans.WriteString("0.")
	count := 2
	for count < 33 && num != 0 {
		num *= 2
		x := byte(num)
		ans.WriteByte('0' + x)
		count++
		num -= float64(x)
	}
	if num == 0 {
		return ans.String()
	}
	return "ERROR"
}

func main() {
	fmt.Printf("printBin(0.1): %v\n", printBin(0.75))
}
