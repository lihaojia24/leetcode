package main

import (
	"fmt"
	"unicode"
)

func helper(ops []int) []int {
	if len(ops) == 1 {
		return ops
	}
	ans := []int{}
	for i := 1; i < len(ops); i += 2 {
		left := helper(ops[:i])
		right := helper(ops[i+1:])
		for _, leftans := range left {
			for _, rightans := range right {
				if ops[i] == -1 {
					ans = append(ans, leftans+rightans)
				} else if ops[i] == -2 {
					ans = append(ans, leftans-rightans)
				} else {
					ans = append(ans, leftans*rightans)
				}
			}
		}
	}
	return ans
}

func diffWaysToCompute(expression string) []int {
	ops := []int{}
	x := 0
	for i := 0; i < len(expression); {
		if unicode.IsDigit(rune(expression[i])) {
			x = 0
			for i < len(expression) && unicode.IsDigit(rune(expression[i])) {
				x *= 10
				x += int(expression[i] - '0')
				i++
			}
			ops = append(ops, x)
		} else {
			if expression[i] == '+' {
				ops = append(ops, -1)
			} else if expression[i] == '-' {
				ops = append(ops, -2)
			} else {
				ops = append(ops, -3)
			}
			i++
		}
	}
	fmt.Printf("ops: %v\n", ops)
	return helper(ops)
}

func main() {
	expression := "2*3-4*5"
	fmt.Printf("diffWaysToCompute(expression): %v\n", diffWaysToCompute(expression))
}
