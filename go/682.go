package main

import "strconv"

func calPoints(operations []string) int {
	res := 0
	stack := []int{}
	for _, op := range operations {
		switch op {
		case "+":
			stack = append(stack, stack[len(stack)-1]+stack[len(stack)-2])
			res += stack[len(stack)-1]
			break
		case "D":
			stack = append(stack, 2*stack[len(stack)-1])
			res += stack[len(stack)-1]
			break
		case "C":
			res -= stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			break
		default:
			pt, _ := strconv.Atoi(op)
			stack = append(stack, pt)
			res += pt
			break
		}
	}
	return res
}
