package main

import (
	"fmt"
)

func search(sSet *[]string, eSet *[]string, bankMap map[string]struct{}) bool {

	eMap := map[string]struct{}{}
	for _, s := range *eSet {
		eMap[s] = struct{}{}
	}
	// fmt.Printf("eMap: %v\n", eMap)
	newSet := []string{}
	for _, s := range *sSet {
		for i, ch := range s {
			// fmt.Printf("\"---\": %v\n", "---")
			for _, v := range "ACGT" {
				if ch != v {
					newS := s[:i] + string(v) + s[i+1:]
					// fmt.Printf("newS: %v\n", newS)
					// v, s := eMap[newS]
					// fmt.Printf("v: %v\n", v)
					// fmt.Printf("s: %v\n", s)
					// if _, ok := eMap[newS]; ok {
					// 	delete(bankMap, newS)
					// 	if _, ok := eMap[newS]; ok {
					// 		return true
					// 	} else {
					// 		newSet = append(newSet, newS)
					// 	}
					// }
					if _, ok := eMap[newS]; ok {
						return true
					} else {
						if _, ok := bankMap[newS]; ok {
							delete(bankMap, newS)
							newSet = append(newSet, newS)
						}
					}
				}
			}
		}
	}
	*sSet = newSet
	return false
}

func minMutation(start string, end string, bank []string) int {
	// s 1
	if start == end {
		return 0
	}
	bankMap := map[string]struct{}{}
	for _, s := range bank {
		bankMap[s] = struct{}{}
	}
	// s 2
	if _, ok := bankMap[end]; !ok {
		return -1
	}
	// delete(bankMap, end)
	// s normal
	startSet, endSet := []string{start}, []string{end}
	startStep, endStep := 0, 0
	for len(startSet) > 0 && len(endSet) > 0 {
		// fmt.Printf("startSet: %v\n", startSet)
		// fmt.Printf("bankMap: %v\n", bankMap)
		// fmt.Printf("endSet: %v\n", endSet)
		if len(startSet) <= len(endSet) {
			startStep++
			if search(&startSet, &endSet, bankMap) {
				return startStep + endStep
			}
		} else {
			endStep++
			if search(&endSet, &startSet, bankMap) {
				return startStep + endStep
			}
		}
	}
	return -1
}

func main() {
	start := "AAAAAAAA"
	end := "CCCCCCCC"
	bank := []string{"AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA", "CCCCCCCC"}
	step := minMutation(start, end, bank)
	fmt.Printf("step: %v\n", step)
}
