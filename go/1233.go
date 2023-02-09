package main

import "sort"

func removeSubfolders(folders []string) (ans []string) {
	sort.Strings(folders)
	ans = append(ans, folders[0])
	for i := 1; i < len(folders); i++ {
		if !match(ans[len(ans)-1], folders[i]) {
			ans = append(ans, folders[i])
		}
	}
	return ans
}

func match(a, b string) bool {
	m, n := len(a), len(b)
	if m < n && a == b[:m] && b[m] == '/' {
		return true
	}
	return false
}

func main() {

}
