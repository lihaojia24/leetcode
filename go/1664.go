package main

// func main() {
// 	nums := []int{1, 1, 1, 1}
// 	fmt.Printf("waysToMakeFair(nums): %v\n", waysToMakeFair(nums))
// }

func waysToMakeFair(nums []int) (ans int) {
	so, se := 0, 0
	to, te := 0, 0
	for i, num := range nums {
		if i%2 == 1 {
			so += num
		} else {
			se += num
		}
	}
	for i, num := range nums {
		if i%2 == 1 {
			// odd == even
			// odd : to + se - te
			// even : te + so - to - num
			if to+se-te == te+so-to-num {
				ans++
			}
		} else {
			// odd : to + se - te - num
			// even : te + so - to
			if to+se-te-num == te+so-to {
				ans++
			}
		}

		if i%2 == 1 {
			to += num
		} else {
			te += num
		}
	}
	return
}
