package main

func main() {

}

func decodeMessage(key string, message string) string {
	m := map[rune]byte{}
	flag := byte('a')
	for _, ch := range key {
		if ch != ' ' && m[ch] == 0 {
			m[ch] = flag
			flag++
		}
	}
	ans := []byte(message)
	for i, ch := range message {
		if ch != ' ' {
			ans[i] = m[ch]
		}
	}
	return string(ans)
}
