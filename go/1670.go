package main

type FrontMiddleBackQueue struct {
	q []int
}

func Constructor() FrontMiddleBackQueue {
	return FrontMiddleBackQueue{q: make([]int, 0)}
}

func (f *FrontMiddleBackQueue) PushFront(val int) {
	f.q = append([]int{val}, f.q...)
}

func (f *FrontMiddleBackQueue) PushMiddle(val int) {
	mid := len(f.q) / 2
	f.q = append(f.q[:mid], append([]int{val}, f.q[mid:]...)...)
}

func (f *FrontMiddleBackQueue) PushBack(val int) {
	f.q = append(f.q, val)
}

func (f *FrontMiddleBackQueue) PopFront() int {
	if len(f.q) == 0 {
		return -1
	}
	val := f.q[0]
	f.q = f.q[1:]
	return val
}

func (f *FrontMiddleBackQueue) PopMiddle() int {
	if len(f.q) == 0 {
		return -1
	}
	mid := (len(f.q) - 1) / 2
	val := f.q[mid]
	f.q = append(f.q[:mid], f.q[mid+1:]...)
	return val
}

func (f *FrontMiddleBackQueue) PopBack() int {
	if len(f.q) == 0 {
		return -1
	}
	val := f.q[len(f.q)-1]
	f.q = f.q[:len(f.q)-1]
	return val
}

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.PushFront(val);
 * obj.PushMiddle(val);
 * obj.PushBack(val);
 * param_4 := obj.PopFront();
 * param_5 := obj.PopMiddle();
 * param_6 := obj.PopBack();
 */
