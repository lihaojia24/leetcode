package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findLUSlength(strs []string) (ans int) {
	ans = -1
nxt:
	for i, child := range strs {
		for j, father := range strs {
			if i == j {
				continue
			}
			childP, fatherP := 0, 0
			for fatherP < len(father) && childP < len(child) {
				if child[childP] == father[fatherP] {
					childP++
					fatherP++
				} else {
					fatherP++
				}
			}
			if childP > len(child)-1 {
				continue nxt
			}
		}
		ans = max(ans, len(child))
	}
	return
}

func main() {
	strs := []string{"abaaa", "cdcc", "eae", "abaaa"}
	fmt.Printf("findLUSlength(strs): %v\n", findLUSlength(strs))
}
