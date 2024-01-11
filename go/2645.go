package main

func addMinimum(word string) (res int) {
	if word[0] == 'b' {
		res += 1
	}
	if word[0] == 'c' {
		res += 2
	}
	for i := range word {
		if i > 0 {
			if word[i-1] == word[i] {
				res += 2
			} else if word[i-1] < word[i] {
				res += int(word[i]-word[i-1]) - 1
			} else {
				if int(word[i-1]-word[i]) == 1 {
					res += 1
				}
			}
		}
	}
	if word[len(word)-1] == 'a' {
		res += 2
	}
	if word[len(word)-1] == 'b' {
		res += 1
	}
	return
}

// "aaaaba"
