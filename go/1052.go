package main

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	res := 0
	no_grumpy_adder := 0
	no_grumpy_adder_max := 0
	for i := range customers {
		if grumpy[i] == 0 {
			res += customers[i]
		} else {
			no_grumpy_adder += customers[i]
		}
		if i >= minutes {
			if grumpy[i-minutes] == 1 {
				no_grumpy_adder -= customers[i-minutes]
			}
		}
		no_grumpy_adder_max = max(no_grumpy_adder, no_grumpy_adder_max)
	}
	return res + no_grumpy_adder_max
}
