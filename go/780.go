package main

import "fmt"

func reachingPoints(sx int, sy int, tx int, ty int) bool {
	for tx > sx && ty > sy && tx != ty {
		if tx > ty {
			tx = tx % ty
		} else {
			ty = ty % tx
		}
	}
	switch {
	case tx == sx && ty == sy:
		return true
	case tx == sx && ty > sy && (ty-sy)%tx == 0:
		return true
	case ty == sy && tx > sx && (tx-sx)%ty == 0:
		return true
	default:
		return false
	}
}

func main() {
	sx := 1
	sy := 1
	tx := 3
	ty := 5
	b := reachingPoints(sx, sy, tx, ty)
	fmt.Printf("b: %v\n", b)
}
