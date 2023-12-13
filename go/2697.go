package main

func makeSmallestPalindrome(s string) string {
	str := []byte(s)
	i := 0
	j := len(str) - 1
	for i < j {
		if str[i] != str[j] {
			if str[i] < str[j] {
				str[j] = str[i]
			} else {
				str[i] = str[j]
			}
		}
		i++
		j--
	}
	return string(str)
}
