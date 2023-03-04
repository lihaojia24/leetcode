package main

import "sort"

func mergeSimilarItems(items1 [][]int, items2 [][]int) (ans [][]int) {
	items := append(items1, items2...)
	sort.Slice(items, func(i, j int) bool {
		return items[i][0] < items[j][0]
	})
	tmp := 0
	for i := 0; i < len(items); i++ {
		tmp = items[i][1]
		if i+1 < len(items) && items[i][0] == items[i+1][0] {
			tmp += items[i+1][1]
			i++
		}
		ans = append(ans, []int{items[i][0], tmp})
	}
	return
}

func main() {

}
