package main

func diStringMatch(s string) (ans []int) {
	left, right := 0, len(s)
	for _, ch := range s {
		if ch == 'I' {
			ans = append(ans, left)
			left++
		} else {
			ans = append(ans, right)
			right--
		}
	}
	ans = append(ans, left)
	return
}

func main() {

}
