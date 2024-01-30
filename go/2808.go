package main

func minimumSeconds(nums []int) int {
	pos_lists := map[int][]int{}
	for index, num := range nums {
		pos_lists[num] = append(pos_lists[num], index)
	}
	n := len(nums)
	res := len(nums)
	for _, pos_list := range pos_lists {
		pos_list = append(pos_list, pos_list[0]+n)
		max_gap := pos_list[1] - pos_list[0]
		for i := 0; i < len(pos_list)-1; i++ {
			max_gap = max(max_gap, pos_list[i+1]-pos_list[i])
		}
		res = min(res, max_gap/2)
	}
	return res
}
