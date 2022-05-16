package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func minStickers(stickers []string, target string) int {
	m := len(target)
	f := make([]int, 1<<m)
	for i := range f {
		f[i] = -1
	}
	f[0] = 0
	var dfs func(lstate int) int
	dfs = func(lstate int) int {
		if f[lstate] != -1 {
			return f[lstate]
		}
		f[lstate] = m + 1
		for _, s := range stickers {
			tmp := lstate
			cnt := make([]int, 26)
			for _, ch := range s {
				cnt[ch-'a']++
			}
			for i, ch := range target {
				if lstate>>i&1 == 1 && cnt[ch-'a'] > 0 {
					cnt[ch-'a']--
					tmp -= (1 << i)
				}
			}
			f[lstate] = min(f[lstate], dfs(tmp)+1)
		}
		return f[lstate]
	}
	ans := dfs(1<<m - 1)
	if ans <= m {
		return ans
	} else {
		return -1
	}
}

func main() {
	ss := []string{"with", "example", "science"}
	t := "thehat"
	fmt.Printf("minStickers(ss, t): %v\n", minStickers(ss, t))
}
