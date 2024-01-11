package main

import (
	"fmt"
	"strconv"
	"strings"
)

func exclusiveTime(n int, logs []string) []int {
	ans := make([]int, n)
	t := []int{}
	s := []int{}
	for _, log := range logs {
		items := strings.Split(log, ":")
		if items[1] == "start" {
			timestamp, _ := strconv.Atoi(items[2])
			t = append(t, timestamp)
			s = append(s, 0)
		} else {
			idx, _ := strconv.Atoi(items[0])
			timestamp, _ := strconv.Atoi(items[2])
			ts := timestamp - t[len(t)-1] + 1
			ts -= s[len(s)-1]
			rm := s[len(s)-1]
			s = s[:len(s)-1]
			if len(s) > 0 {
				s[len(s)-1] += rm
				s[len(s)-1] += ts
			}
			ans[idx] += ts
			t = t[:len(t)-1]
		}
		fmt.Printf("t: %v\n", t)
		fmt.Printf("s: %v\n", s)
		fmt.Printf("ans: %v\n", ans)
	}
	return ans
}

// func main() {
// 	n := 1
// 	logs := []string{"0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"}
// 	fmt.Printf("exclusiveTime(n, logs): %v\n", exclusiveTime(n, logs))
// }
