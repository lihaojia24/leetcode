package main

import "fmt"

type MagicDictionary struct {
	m map[int][]string
}

func Constructor() MagicDictionary {
	return MagicDictionary{make(map[int][]string)}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	for _, word := range dictionary {
		if _, ok := this.m[len(word)]; ok {
			this.m[len(word)] = append(this.m[len(word)], word)
		} else {
			this.m[len(word)] = []string{word}
		}
	}
	// fmt.Printf("this.m: %v\n", this.m)
}

func match(a, b string) int {
	ans := 0
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			ans++
		}
	}
	return ans
}

func (this *MagicDictionary) Search(searchWord string) bool {
	for _, word := range this.m[len(searchWord)] {
		if match(word, searchWord) == 1 {
			return true
		}
	}
	return false
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
 */

func main() {
	dictionary := []string{"nihao", "hello", "leetcode"}
	obj := Constructor()
	obj.BuildDict(dictionary)
	param_1 := obj.Search("niha")
	param_2 := obj.Search("niha1")
	fmt.Printf("param_1: %v\n", param_1)
	fmt.Printf("param_2: %v\n", param_2)
}
