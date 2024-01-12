package main

func heightChecker(heights []int) (ans int) {
	m := [101]int{}
	for _, v := range heights {
		m[v]++
	}
	index := 0
	for num, count := range m {
		for i := 0; i < count; i++ {
			if heights[index] != num {
				ans++
			}
			index++
		}
	}
	return
}

// func main() {
// 	heights := []int{1, 1, 4, 2, 1, 3}
// 	fmt.Printf("heightChecker(heights): %v\n", heightChecker(heights))
// }
