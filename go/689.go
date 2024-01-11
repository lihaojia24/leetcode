package main

import "fmt"

func maxSumOfThreeSubarrays(nums []int, k int) []int {
	n := len(nums)
	sums := make([]int, n-k+1)
	for i := 0; i < k; i++ {
		sums[0] += nums[i]
	}
	for i := k; i < n; i++ {
		sums[i-k+1] = sums[i-k] + nums[i] - nums[i-k]
	}

	type node struct {
		s    int
		preI int
		i    int
	}
	one := make([]node, len(sums))
	two := make([]node, len(sums))
	three := make([]node, len(sums))
	one[0] = node{preI: -1, i: 0, s: sums[0]}
	two[k] = node{preI: 0, i: k, s: one[0].s + sums[k]}
	three[2*k] = node{preI: k, i: 2 * k, s: two[k].s + sums[2*k]}
	for i := 1; i < len(sums); i++ {
		if sums[i] > one[i-1].s {
			one[i] = node{preI: -1, i: i, s: sums[i]}
		} else {
			one[i] = one[i-1]
		}
		if i > k {
			if sums[i]+one[i-k].s > two[i-1].s {
				two[i] = node{preI: one[i-k].i, i: i, s: sums[i] + one[i-k].s}
			} else {
				two[i] = two[i-1]
			}
		}
		if i > 2*k {
			if sums[i]+two[i-k].s > three[i-1].s {
				three[i] = node{preI: two[i-k].i, i: i, s: sums[i] + two[i-k].s}
			} else {
				three[i] = three[i-1]
			}
		}
	}
	fmt.Printf("sums: %v\n", sums)
	fmt.Printf("one: %v\n", one)
	fmt.Printf("two: %v\n", two)
	fmt.Printf("three: %v\n", three)
	fmt.Printf("three[len(sums)].i: %v\n", three[len(sums)-1].i)
	fmt.Printf("three[len(sums)].preI: %v\n", three[len(sums)-1].preI)
	fmt.Printf("two[three[len(sums)].preI].preI: %v\n", two[three[len(sums)-1].preI].preI)
	return []int{two[three[len(sums)-1].preI].preI, three[len(sums)-1].preI, three[len(sums)-1].i}
}

// func main() {
// 	nums := []int{7, 13, 20, 19, 19, 2, 10, 1, 1, 19}
// 	k := 3
// 	maxSumOfThreeSubarrays(nums, k)
// }
