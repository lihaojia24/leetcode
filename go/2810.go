package main

import "slices"

func finalString(s string) string {
	q := [2][]rune{}
	dir := 1
	for _, ch := range s {
		if ch == 'i' {
			dir ^= 1
		} else {
			q[dir] = append(q[dir], ch)
		}
	}
	slices.Reverse(q[dir^1])
	return string(append(q[dir^1], q[dir]...))
}
