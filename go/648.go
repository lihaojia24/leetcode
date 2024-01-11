package main

type dicTree struct {
	m      map[rune]*dicTree
	isLeaf bool
}

func replaceWords(dictionary []string, sentence string) string {
	root := &dicTree{m: map[rune]*dicTree{}}
	for _, dic := range dictionary {
		node := root
		for _, ch := range dic {
			if node.m[ch] == nil {
				node.m[ch] = &dicTree{m: map[rune]*dicTree{}}
			}
			node = node.m[ch]
		}
		node.isLeaf = true
	}
	ans := ""
	for i := 0; i < len(sentence); {
		start := i
		for i < len(sentence) && sentence[i] != ' ' {
			i++
		}
		str := sentence[start:i]
		i++
		node := root
		for idx, ch := range str {
			node = node.m[ch]
			if node != nil {
				if node.isLeaf {
					ans += str[:idx+1] + " "
					break
				}
			} else {
				ans += str + " "
				break
			}
		}
		if node != nil && !node.isLeaf {
			ans += str + " "
		}
	}
	return ans[:len(ans)-1]
}

// func main() {
// 	dictionary := []string{"a", "aa", "aaa", "aaaa"}
// 	sentence := "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
// 	fmt.Printf("replaceWords(dictionary, sentence): %v\n", replaceWords(dictionary, sentence))
// }
