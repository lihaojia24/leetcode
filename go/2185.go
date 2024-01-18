package main

func prefixCount(words []string, pref string) (ans int) {

	var match func(word string) bool
	match = func(word string) bool {
		index := 0
		if len(word) < len(pref) {
			return false
		}
		for index < len(pref) {
			if pref[index] != word[index] {
				return false
			}
			index++
		}
		return true
	}
	for _, word := range words {
		if match(word) {
			ans++
		}
	}
	return
}
