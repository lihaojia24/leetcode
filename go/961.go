package main

func repeatedNTimes(nums []int) int {
	for index, num := range nums {
		if index > 0 && nums[index-1] == num {
			return num
		}
		if index > 1 && nums[index-2] == num {
			return num
		}
		if index > 2 && nums[index-3] == num {
			return num
		}
	}
	return -1
}

func main() {

}
