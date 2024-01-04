package main

func canSeePersonsCount(heights []int) []int {
	n := len(heights)
	ans := make([]int, n)
	q := []int{heights[n-1]}
	for i := n - 2; i > -1; i-- {
		d := 0
		for len(q)-d > 0 && q[len(q)-1-d] <= heights[i] {
			d++
		}
		ans[i] = d
		if len(q)-d != 0 {
			ans[i]++
		}
		q = q[:len(q)-d]
		q = append(q, heights[i])
	}
	return ans
}

// func main() {
// 	h := []int{10, 6, 8, 5, 11, 9}
// 	fmt.Printf("canSeePersonsCount(h): %v\n", canSeePersonsCount(h))
// }
