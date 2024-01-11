package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	i := 0
	l := len(flowerbed)
	ans := 0
	for i < l {
		if flowerbed[i] == 0 {
			if i == l-1 || flowerbed[i+1] == 0 {
				ans += 1
				i += 2
			} else {
				i += 1
			}
		} else {
			i += 2
		}
	}
	return ans >= n
}
