package main

func findOriginalArray(changed []int) []int {
	cnt := map[int]int{}
	for _, num := range changed {
		cnt[num]++
	}
	cnt0 := cnt[0]
	if cnt0%2 == 1 {
		return nil
	}
	delete(cnt, 0)
	ans := make([]int, cnt0/2, len(changed)/2)
	done := map[int]bool{}
	for x := range cnt {
		if done[x] || x%2 == 0 && cnt[x/2] > 0 {
			continue
		}
		for cnt[x] > 0 {
			cntX := cnt[x]
			if cntX > cnt[2*x] {
				return nil
			}
			for i := 0; i < cntX; i++ {
				ans = append(ans, x)
			}
			done[x] = true
			cnt[2*x] -= cntX
			if cnt[2*x] == 0 {
				done[2*x] = true
				x *= 4
			} else {
				x *= 2
			}
		}
	}
	return ans
}
