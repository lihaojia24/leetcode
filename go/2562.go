package main

func findTheArrayConcVal(nums []int) (ans int64) {
	i, j := 0, len(nums)-1
	for i <= j {
		if i == j {
			ans += int64(nums[i])
		} else {
			a := nums[i]
			b := nums[j]
			for b > 0 {
				a *= 10
				b /= 10
			}
			ans += int64(a + nums[j])
		}
		i += 1
		j -= 1
	}
	return
}

func main() {

}
