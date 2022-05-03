package main

import (
	"sort"
	"strings"
	"unicode"
)

func reorderLogFiles(logs []string) []string {
	sort.SliceStable(logs, func(i, j int) bool {
		log1, log2 := logs[i], logs[j]
		log1end, log2end := strings.SplitN(log1, " ", 2)[1], strings.SplitN(log2, " ", 2)[1]
		isDlog1, isDlog2 := unicode.IsDigit(rune(log1end[0])), unicode.IsDigit(rune(log2end[0]))
		if isDlog1 && isDlog2 {
			return false
		}
		if !isDlog1 && !isDlog2 {
			return log1end < log2end || log1end == log2end && log1 < log2
		}
		return !isDlog1
	})
	return logs
}

func main() {

}
