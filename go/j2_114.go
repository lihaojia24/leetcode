package main

func alienOrder(words []string) string {
	// 构造有向图
	m := map[byte][]byte{}
	// 1 visiting 2 visited
	state := map[byte]int{}
	for _, ch := range words[0] {
		state[byte(ch)] = 0
	}
next:
	for i := 1; i < len(words); i++ {
		for _, ch := range words[i] {
			state[byte(ch)] = 0
		}
		pre, word := words[i-1], words[i]
		for j := 0; j < len(pre) && j < len(word); j++ {
			if pre[j] != word[j] {
				m[pre[j]] = append(m[pre[j]], word[j])
				continue next
			}
		}
		if len(pre) > len(word) {
			return ""
		}
	}
	// DFS
	ans := make([]byte, len(state))
	index := len(ans) - 1
	var dfs func(byte) bool
	dfs = func(ch byte) bool {
		state[ch] = 1
		for _, nxt := range m[ch] {
			if state[nxt] == 1 {
				return false
			} else if state[nxt] == 0 {
				if !dfs(nxt) {
					return false
				}
			}
		}
		state[ch] = 2
		ans[index] = ch
		index--
		return true
	}

	for ch := range state {
		if state[ch] == 0 && !dfs(ch) {
			return ""
		}
	}
	return string(ans)
}

func alienOrderBFS(words []string) string {
	// 构造有向图
	m := map[byte][]byte{}
	inDeg := map[byte]int{}
	for _, ch := range words[0] {
		inDeg[byte(ch)] = 0
	}
next:
	for i := 1; i < len(words); i++ {
		pre, word := words[i-1], words[i]
		for _, ch := range word {
			inDeg[byte(ch)] = inDeg[byte(ch)] + 0
		}
		for j := 0; j < len(word) && j < len(pre); j++ {
			if pre[j] != word[j] {
				m[pre[j]] = append(m[pre[j]], word[j])
				inDeg[word[j]]++
				continue next
			}
		}
		if len(pre) > len(word) {
			return ""
		}
	}

	// BFS
	ans := make([]byte, len(inDeg))
	index := 0
next2:
	for index < len(ans) {
		for ch := range inDeg {
			if inDeg[ch] == 0 {
				delete(inDeg, ch)
				ans[index] = ch
				index++
				for _, nxt := range m[ch] {
					inDeg[nxt]--
				}
				continue next2
			}
		}
		return ""
	}
	return string(ans)
}

// func main() {
// 	words := []string{"wrt", "wrf", "er", "ett", "rftt"}
// 	for i := 0; i < 50; i++ {
// 		fmt.Printf("alienOrder(words): %v\n", alienOrderBFS(words))
// 	}

// }
