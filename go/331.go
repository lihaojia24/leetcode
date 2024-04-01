package main

import (
	"strings"
)

func isValidSerialization(preorder string) bool {
	st := make([]string, 0)
	nodes := strings.Split(preorder, ",")
	for _, node := range nodes {
		st = append(st, node)
		for len(st) > 2 && st[len(st)-1] == "#" && st[len(st)-2] == "#" && st[len(st)-3] != "#" {
			st = st[:len(st)-3]
			st = append(st, "#")
		}
	}
	return len(st) == 1 && st[0] == "#"
}
