package main

func min(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func findClosest(words []string, word1 string, word2 string) (ans int) {
	index1, index2 := -1, -1
	ans = len(words)
	for i, word := range words {
		if word == word1 {
			index1 = i
			if index2 >= 0 {
				ans = min(ans, index1-index2)
			}
		}
		if word == word2 {
			index2 = i
			if index1 >= 0 {
				ans = min(ans, index2-index1)
			}
		}
	}
	return ans
}

func main() {

}
