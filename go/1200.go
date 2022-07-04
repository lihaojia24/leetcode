package main

import "sort"

func minimumAbsDifference(arr []int) [][]int {
	sort.Slice(arr, func(i, j int) bool {
		return arr[i] < arr[j]
	})
	gap := arr[1] - arr[0]
	ans := []int{arr[0]}
	for i := 1; i < len(arr)-1; i++ {
		if arr[i+1]-arr[i] < gap {
			gap = arr[i+1] - arr[i]
			ans = []int{arr[i]}
		} else if arr[i+1]-arr[i] == gap {
			ans = append(ans, arr[i])
		}
	}
	res := [][]int{}
	for _, v := range ans {
		res = append(res, []int{v, v + gap})
	}
	return res
}

func main() {

}
