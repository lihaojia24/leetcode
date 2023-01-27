package main

import (
	"strings"
	"unicode"
)

func main() {

}

func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}
	flags := [4]int{}
	for i, ch := range password {
		if i > 0 && password[i] == password[i-1] {
			return false
		}
		if unicode.IsLower(ch) {
			flags[0] = 1
		}
		if unicode.IsUpper(ch) {
			flags[1] = 1
		}
		if unicode.IsDigit(ch) {
			flags[2] = 1
		}
		if strings.ContainsRune("!@#$%^&*()-+", ch) {
			flags[3] = 1
		}
	}
	return flags[0]+flags[1]+flags[2]+flags[3] == 4
}
