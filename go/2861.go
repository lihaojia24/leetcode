package main

func minL(nums []int) int {
	res := nums[0]
	for _, num := range nums {
		res = min(num, res)
	}
	return res
}

func maxNumberOfAlloys(n int, k int, budget int, compositions [][]int, stock []int, cost []int) (res int) {
	for _, comp := range compositions {
		l, r := 0, minL(stock)+budget
		for l < r {
			m := (l+r)/2 + 1
			need := 0
			for i, cost_i := range cost {
				need += cost_i * max(0, (m*comp[i]-stock[i]))
			}
			if need > budget {
				r = m - 1
			} else {
				l = m
			}
			// fmt.Printf("need: %v\n", need)
		}
		// fmt.Printf("comp: %v\n", comp)
		// fmt.Printf("l: %v\n", l)
		res = max(res, l)
	}
	return
}

// func main() {
// 	com := [][]int{[]int{1, 1, 1}, []int{1, 1, 10}}
// 	stock := []int{0, 0, 100}
// 	cost := []int{1, 2, 3}
// 	maxNumberOfAlloys(3, 2, 15, com, stock, cost)
// }
