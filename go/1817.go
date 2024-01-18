package main

func findingUsersActiveMinutes(logs [][]int, k int) []int {
	ansSet := map[int]map[int]bool{}
	for _, log := range logs {
		if ansSet[log[0]] == nil {
			ansSet[log[0]] = map[int]bool{}
		}
		ansSet[log[0]][log[1]] = true
	}
	ans := make([]int, k+1)
	for _, v := range ansSet {
		ans[len(v)]++
	}
	return ans[1:]
}
