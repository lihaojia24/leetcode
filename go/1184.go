package main

func distanceBetweenBusStops(distance []int, start int, destination int) int {
	if start > destination {
		start, destination = destination, start
	}
	ans1, ans2 := 0, 0
	n := len(distance)
	for i := 0; i < n; i++ {
		if start <= i && i < destination {
			ans1 += distance[i]
		} else {
			ans2 += distance[i]
		}
	}
	if ans1 < ans2 {
		return ans1
	} else {
		return ans2
	}
}
