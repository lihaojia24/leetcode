package main

func lengthLongestPath(input string) (ans int) {
	n := len(input)
	lengthStack := []int{}
	for i := 0; i < n; {
		depth := 1
		for ; i < n && input[i] == '\t'; i++ {
			depth++
		}
		lenght, isFile := 0, false
		for ; i < n && input[i] != '\n'; i++ {
			if input[i] == '.' {
				isFile = true
			}
			lenght++
		}
		i++
		if depth <= len(lengthStack) {
			lengthStack = lengthStack[:depth-1]
		}
		if len(lengthStack) > 0 {
			lenght += lengthStack[len(lengthStack)-1] + 1
		}
		if isFile {
			ans = max(ans, lenght)
		} else {
			lengthStack = append(lengthStack, lenght)
		}
	}
	return
}
