package main

import "fmt"

func findSubstring(s string, words []string) (ans []int) {
	sLen := len(s)
	wordLen := len(words[0])
	wordNum := len(words)
	hs := map[string]int{}
	for _, word := range words {
		hs[word]++
	}
	fmt.Printf("hs: %v\n", hs)
	for start := 0; start < wordLen; start++ {
		l, count := start, 0
		ths := map[string]int{}
		for l+count*wordLen+wordLen < sLen+1 {
			if l == 13 {
				// fmt.Println("---------------------------")
				// fmt.Printf("count: %v\n", count)
			}
			flag := false
			//处理新加的单次
			if count < wordNum {
				tword := s[l+count*wordLen : l+count*wordLen+wordLen]
				fmt.Printf("tword: %v\n", tword)
				// fmt.Printf("ths: %v\n", ths)
				// ths[tword]++
				if ths[tword] < hs[tword] {
					ths[tword]++
					count++
					if ths[tword] == hs[tword] && count == wordNum {
						ans = append(ans, l)
						//shan chu qian bian
						// fmt.Println(1)
						flag = true
					}
				} else {
					// 添加后单次重复
					// fmt.Println(2)
					flag = true
				}
			} else {
				// 过长
				// fmt.Println(3)
				flag = true
			}
			//减掉最前端单次
			if flag {
				if count > 0 {
					count--
					sword := s[l : l+wordLen]
					ths[sword]--
					l += wordLen
				} else {
					ths = map[string]int{}
					l += wordLen
				}
			}
		}
	}
	return ans
}

func main() {
	s := "a"
	words := []string{"a"}
	fmt.Printf("findSubstring(s, words): %v\n", findSubstring(s, words))
}
