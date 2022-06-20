package main

import "fmt"

type pair struct {
	num  int
	lazy bool
}

type RangeModule map[int]pair

func Constructor() RangeModule {
	return RangeModule{}
}

// left, right 修改区间
// l, r 处理区间
// lazy 1  0  -1
func (this RangeModule) update(left, right, l, r, idx, tag int) {
	// 不在区间内
	if left > r || right < l {
		return
	}
	// 全部在区间内
	if left <= l && r <= right {
		p := this[idx]
		p.num = tag
		p.lazy = true
		this[idx] = p
	} else {
		//部分
		mid := (l + r) / 2
		//下传lazy
		this.downPut(idx)
		//update子树
		this.update(left, right, l, mid, idx*2, tag)
		this.update(left, right, mid+1, r, idx*2+1, tag)
		//回传数值
		p := this[idx]
		if this[idx*2].num == 1 && this[idx*2+1].num == 1 {
			p.num = 1
		} else {
			p.num = 0
		}
		this[idx] = p
	}
}

func (this RangeModule) downPut(idx int) {
	p := this[idx]
	if this[idx].lazy {
		pLeft := this[idx*2]
		pRight := this[idx*2+1]
		pLeft.lazy = true
		pLeft.num = p.num
		pRight.lazy = true
		pRight.num = p.num
		this[idx*2] = pLeft
		this[idx*2+1] = pRight
		p.lazy = false
		this[idx] = p
	}
}

func (this RangeModule) query(left, right, l, r, idx int) bool {
	if left > r || right < l {
		return true
	}
	if left <= l && r <= right {
		return this[idx].num == 1
	} else {
		mid := (l + r) / 2
		//下传lazy
		this.downPut(idx)
		lNum := this.query(left, right, l, mid, idx*2)
		rNum := this.query(left, right, mid+1, r, idx*2+1)
		return lNum && rNum
	}
}

func (this RangeModule) AddRange(left int, right int) {
	this.update(left, right-1, 0, 1e9, 1, 1)
}

func (this RangeModule) QueryRange(left int, right int) bool {
	return this.query(left, right-1, 0, 1e9, 1)
}

func (this RangeModule) RemoveRange(left int, right int) {
	this.update(left, right-1, 0, 1e9, 1, 0)
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRange(left,right);
 * param_2 := obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */

func main() {
	obj := Constructor()
	obj.AddRange(1, 18)
	obj.AddRange(15, 20)
	obj.AddRange(25, 50)
	// obj.RemoveRange(14, 16)
	// i := obj.QueryRange(5, 10)
	// fmt.Printf("i: %v\n", i)
	i := obj.QueryRange(18, 30)
	fmt.Printf("i: %v\n", i)
	// i = obj.QueryRange(16, 17)
	// fmt.Printf("i: %v\n", i)
}
