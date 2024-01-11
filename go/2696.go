package main

func minLength(s string) (res int) {
	st := []rune{}
	for _, ch := range s {
		st = append(st, ch)
		n := len(st)
		if n > 1 && (string(st[n-2:n]) == "AB" || string(st[n-2:n]) == "CD") {
			st = st[:n-2]
		}
	}
	return len(st)
}

// func main() {
// 	s := "ABFCACDB"
// 	minLength(s)
// }
