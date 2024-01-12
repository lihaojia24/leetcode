package main

func removeOuterParentheses(s string) string {
	leftCnt := 0
	ans := []rune{}
	for _, ch := range s {
		// fmt.Printf("ch: %v\n", ch)
		if ch == '(' {
			leftCnt++
			if leftCnt == 1 {
				continue
			}
		}
		if ch == ')' {
			leftCnt--
			if leftCnt == 0 {
				continue
			}
		}
		ans = append(ans, ch)
	}
	return string(ans)

}

// func main() {
// 	s := "(()())(())(()(()))"
// 	fmt.Printf("removeOuterParentheses(s): %v\n", removeOuterParentheses(s))
// }
