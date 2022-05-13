package main

import "fmt"

func oneEditAway(first string, second string) bool {
	dis := len(first) - len(second)
	if dis != 0 && dis != 1 && dis != -1 {
		return false
	}
	i, j := 0, 0
	dif := 0
	for i < len(first) && j < len(second) {
		if first[i] == second[j] {
			i++
			j++
		} else {
			if dif != 0 {
				return false
			} else {
				dif++
				if dis == 0 {
					i++
					j++
				} else if dis == 1 {
					i++
				} else {
					j++
				}
			}
		}
	}
	return true
}

func main() {
	first := "abcdds"
	second := "abcdd"
	fmt.Printf("oneEditAway(first, second): %v\n", oneEditAway(first, second))
}
