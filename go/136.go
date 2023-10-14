package main

func singleNumber(nums []int) (ans int) {
	for _, num := range nums {
		ans ^= num
	}
	return
}

func main() {

}
