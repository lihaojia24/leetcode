package main

func countTriplets(nums []int) (ans int) {
	cnt := [1 << 16]int{}
	for _, a := range nums {
		for _, b := range nums {
			cnt[a&b]++
		}
	}
	for x, n := range cnt {
		for _, c := range nums {
			if x&c == 0 {
				ans += n
			}
		}
	}
	return ans
}

// func main() {

// }
