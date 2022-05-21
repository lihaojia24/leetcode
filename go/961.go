package main

func repeatedNTimes(nums []int) int {
	for index, num := range nums {
		if index > 0 && nums[index-1] == ans {
			return num
		}
		if index > 1 && nums[index-2] == ans {
			return num
		}
		if index > 2 && nums[index-3] == ans {
			return num
		}
	}
	return -1
}

func main() {

}
