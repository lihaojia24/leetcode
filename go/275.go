package main

func hIndex(citations []int) int {
	n := len(citations)
	l, r := 0, n-1
	if citations[r] == 0 {
		return 0
	}
	var mid int
	var t int
	var x int
	for l < r {
		mid = (l + r) >> 1
		t = citations[mid]
		x = n - mid
		if x <= t {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return n - l
}

func main() {

}
