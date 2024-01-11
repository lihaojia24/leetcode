package main

type MyCircularQueue struct {
	nums  []int
	start int
	next  int
	full  bool
}

func Constructor22(k int) MyCircularQueue {
	return MyCircularQueue{nums: make([]int, k)}
}

func (this *MyCircularQueue) EnQueue(value int) bool {
	if this.start == this.next && this.full {
		return false
	}
	this.nums[this.next] = value
	this.next++
	this.next %= len(this.nums)
	if this.start == this.next {
		this.full = true
	}
	return true
}

func (this *MyCircularQueue) DeQueue() bool {
	if this.start == this.next && !this.full {
		return false
	}
	this.start++
	this.start %= len(this.nums)
	if this.start == this.next {
		this.full = false
	}
	return true
}

func (this *MyCircularQueue) Front() int {
	if this.start == this.next && !this.full {
		return -1
	}
	return this.nums[this.start]
}

func (this *MyCircularQueue) Rear() int {
	if this.start == this.next && !this.full {
		return -1
	}
	return this.nums[(this.next-1+len(this.nums))%len(this.nums)]
}

func (this *MyCircularQueue) IsEmpty() bool {
	if this.start == this.next && !this.full {
		return true
	}
	return false
}

func (this *MyCircularQueue) IsFull() bool {
	if this.start == this.next && this.full {
		return true
	}
	return false
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
 */

// func main() {

// }
