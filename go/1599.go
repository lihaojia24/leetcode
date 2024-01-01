package main

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	if boardingCost*4 < runningCost {
		return -1
	}
	remain := 0
	for i := range customers {
		if customers[i] >= 4 {
			remain += customers[i] - 4
			customers[i] = 4
		} else {
			if customers[i]+remain >= 4 {
				remain -= 4 - customers[i]
				customers[i] = 4
			} else {
				customers[i] += remain
				remain = 0
			}
		}
	}
	for remain > 0 {
		if remain >= 4 {
			customers = append(customers, 4)
			remain -= 4
		} else {
			customers = append(customers, remain)
			remain = 0
		}
	}
	ans := -1
	ansT := 0
	tmp := 0
	for i, x := range customers {
		tmp += boardingCost*x - runningCost
		if tmp > 0 && tmp > ansT {
			ansT = tmp
			ans = i
		}
	}
	return ans
}
