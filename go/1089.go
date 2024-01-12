package main

func duplicateZeros(arr []int) {
	i, j := 0, -1
	n := len(arr)
	for index, num := range arr {
		j++
		if num == 0 {
			j++
		}
		if j == n-1 {
			i = index
			break
		}
		if j > n-1 {
			i = index - 1
			j--
			arr[j] = 0
			j--
			break
		}
	}
	for index := i; index >= 0; index-- {
		arr[j] = arr[index]
		j--
		if arr[index] == 0 {
			arr[j] = arr[index]
			j--
		}
	}
	return
}

// func main() {
// 	arr := []int{1, 2, 3}
// 	duplicateZeros(arr)
// 	fmt.Printf("arr: %v\n", arr)
// }
