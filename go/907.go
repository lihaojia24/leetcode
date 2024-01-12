package main

func sumSubarrayMins(arr []int) int {
	n := len(arr)
	left := make([]int, n)
	st := []int{-1}
	for i, num := range arr {
		for len(st) > 1 && arr[st[len(st)-1]] >= num {
			st = st[:len(st)-1]
		}
		left[i] = st[len(st)-1]
		st = append(st, i)
	}
	right := make([]int, n)
	st = []int{n}
	for i := n - 1; i >= 0; i-- {
		for len(st) > 1 && arr[st[len(st)-1]] > arr[i] {
			st = st[:len(st)-1]
		}
		right[i] = st[len(st)-1]
		st = append(st, i)
	}
	ans := 0
	for i, num := range arr {
		ans += (i - left[i]) * (right[i] - i) * num
	}
	return ans % (1_000_000_000 + 7)
}
