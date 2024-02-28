package main

import "fmt"

func minIncrements(n int, cost []int) int {
	added := 0
	var helper func(node int) (s int)
	helper = func(node int) (s int) {
		if 2*node > n {
			return cost[node-1]
		}
		left := helper(2 * node)
		right := helper(2*node + 1)
		fmt.Printf("node: %v\n", node)
		// fmt.Printf("left: %v\n", left)
		// fmt.Printf("right: %v\n", right)
		if left > right {
			added += left - right
			fmt.Printf("added: %v\n", left-right)
			return cost[node-1] + left
		} else {
			added += right - left
			fmt.Printf("added: %v\n", right-left)
			return cost[node-1] + right
		}
	}
	helper(1)
	return added
}

// func main() {
// 	n := 15
// 	cost := []int{764, 1460, 2664, 764, 2725, 4556, 5305, 8829, 5064, 5929, 7660, 6321, 4830, 7055, 3761}
// 	minIncrements(n, cost)
// }
