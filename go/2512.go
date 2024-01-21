package main

import (
	"sort"
	"strings"
)

func topStudents(positive_feedback []string, negative_feedback []string, report []string, student_id []int, k int) []int {
	score := map[string]int{}
	for _, w := range positive_feedback {
		score[w] = 3
	}
	for _, w := range negative_feedback {
		score[w] = -1
	}
	type pair struct{ score, id int }
	students := make([]pair, len(report))
	for i, r := range report {
		s := 0
		for _, w := range strings.Split(r, " ") {
			s += score[w]
		}
		students[i] = pair{s, student_id[i]}
	}
	sort.Slice(students, func(i, j int) bool {
		a, b := students[i], students[j]
		if a.score == b.score {
			return a.id < b.id
		}
		return a.score > b.score
	})
	ans := make([]int, k)
	for i, p := range students[:k] {
		ans[i] = p.id
	}
	return ans
}
