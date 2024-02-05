package main

func magicTower(nums []int) int {
	s := 1
	for _, num := range nums {
		s += num
	}
	if s <= 0 {
		return -1
	}
	ans := 0
	st := []int{}
	s = 1
	var get_min_index func(nums []int) int
	get_min_index = func(nums []int) int {
		res := 0
		m := nums[0]
		for i, num := range nums {
			if num < m {
				m = num
				res = i
			}
		}
		return res
	}

	for _, num := range nums {
		if num < 0 {
			st = append(st, num)
		}
		s += num
		for s <= 0 {
			ans++
			min_index := get_min_index(st)
			s -= st[min_index]
			st = append(st[:min_index], st[min_index+1:]...)
		}
	}
	return ans
}
