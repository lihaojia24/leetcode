package main

type NumArray struct {
	nums []int
	sums []int
}

func Constructor(nums []int) NumArray {
	n := len(nums)
	a := NumArray{make([]int, n), make([]int, n+1)}
	for index, num := range nums {
		a.Update(index, num)
	}
	return a
}

func (this *NumArray) Update(index int, val int) {
	delta := val - this.nums[index]
	this.nums[index] = val
	index += 1
	for i := index; i < len(this.sums); i += i & -i {
		this.sums[i] += delta
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefixSum(left+1-1) - this.prefixSum(right+1)
}

func (this *NumArray) prefixSum(index int) (s int) {
	for i := index; i > 0; i -= i & -i {
		s += this.sums[i]
	}
	return
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */
