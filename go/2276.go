package main

import "github.com/emirpasic/gods/trees/redblacktree"

// type CountIntervals struct {
// 	l, r, cnt   int
// 	left, right *CountIntervals
// }

// func Constructor() CountIntervals {
// 	return CountIntervals{l: 1, r: 1_000_000_000}
// }

// func (c *CountIntervals) Add(l int, r int) {
// 	if c.cnt == c.r-c.r+1 {
// 		return
// 	}
// 	if l <= c.l && c.r <= r {
// 		c.cnt = c.r - c.l + 1
// 		return
// 	}
// 	mid := (c.l + c.r) / 2
// 	if c.left == nil {
// 		c.left = &CountIntervals{l: c.l, r: mid}
// 	}
// 	if c.right == nil {
// 		c.right = &CountIntervals{l: mid + 1, r: c.r}
// 	}
// 	if l <= mid {
// 		c.left.Add(l, r)
// 	}
// 	if r >= mid+1 {
// 		c.right.Add(l, r)
// 	}
// 	c.cnt = c.left.cnt + c.right.cnt
// }

// func (c *CountIntervals) Count() int {
// 	return c.cnt
// }

/**
 * Your CountIntervals object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(left,right);
 * param_2 := obj.Count();
 */

type CountIntervals struct {
	*redblacktree.Tree
	cnt int
}

func Constructor() CountIntervals {
	return CountIntervals{redblacktree.NewWithIntComparator(), 0}
}

func (c *CountIntervals) Add(left int, right int) {
	for node, _ := c.Ceiling(left); node != nil && node.Value.(int) <= right; node, _ = c.Ceiling(left) {
		l, r := node.Value.(int), node.Key.(int)
		if l < left {
			left = l
		}
		if r > right {
			right = r
		}
		c.cnt -= r - l + 1
		c.Remove(r)
	}
	c.cnt += right - left + 1
	c.Put(right, left)
}

func (c *CountIntervals) Count() int {
	return c.cnt
}
