package main

func maxResult(nums []int, k int) int {
	n := len(nums)
	res := make([]int, n)
	res[0] = nums[0]
	st := []int{0}
	for i := 1; i < n; i++ {
		if i-st[0] > k {
			st = st[1:]
		}
		res[i] = res[st[0]] + nums[i]
		for len(st) > 0 && res[st[len(st)-1]] <= res[i] {
			st = st[:len(st)-1]
		}
		st = append(st, i)
	}
	// fmt.Printf("res: %v\n", res)
	return res[n-1]
}

func main() {
	nums := []int{10, -5, -2, 4, 0, 3}
	k := 3
	maxResult(nums, k)
}
