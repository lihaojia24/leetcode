package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

type pair struct{ num, lazy int }

type MyCalendarThree map[int]pair

func Constructor() MyCalendarThree {
	return MyCalendarThree{}
}

//节点所在区间 l r
//需要修改区间 start end
//idx start from 1
//father idx // 2
//left child idx * 2
//right child idx * 2 + 1
func (this MyCalendarThree) update(start, end, l, r, idx int) {
	//节点区间不在修改范围内
	if start > r || end < l {
		return
	}
	//节点区间全在修改范围内
	if start <= l && r <= end {
		p := this[idx]
		p.num++
		p.lazy++
		this[idx] = p
	} else {
		//节点区间一部分在修改范围内
		mid := (l + r) / 2
		this.update(start, end, l, mid, idx*2)
		this.update(start, end, mid+1, r, idx*2+1)
		p := this[idx]
		// p.num = this[idx*2].num + this[idx*2+1].num + this[idx].lazy
		p.num = max(this[idx*2].num, this[idx*2+1].num) + p.lazy
		this[idx] = p
	}
}

func (this MyCalendarThree) Book(start int, end int) int {
	this.update(start, end-1, 0, 1e9, 1)
	return this[1].num
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */

func main() {
	t := Constructor()
	fmt.Printf("t.Book(10, 20): %v\n", t.Book(10, 20))
	fmt.Printf("t.Book(50, 60): %v\n", t.Book(50, 60))
}
