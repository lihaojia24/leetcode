package main

import "container/heap"

type StockPrice struct {
	cur          int
	tMap         map[int]int
	hpMax, hpMin hp
}

func Constructor() StockPrice {
	return StockPrice{tMap: map[int]int{}}
}

func (this *StockPrice) Update(timestamp int, price int) {
	heap.Push(&this.hpMax, pair{-price, timestamp})
	heap.Push(&this.hpMin, pair{price, timestamp})
	this.tMap[timestamp] = price
	if timestamp > this.cur {
		this.cur = timestamp
	}
}

func (this *StockPrice) Current() int {
	return this.tMap[this.cur]
}

func (this *StockPrice) Maximum() int {
	for {
		if p := this.hpMax[0]; p.price == this.tMap[p.timestamp] {
			return -p.price
		}
		heap.Pop(&this.hpMax)
	}
}

func (this *StockPrice) Minimum() int {
	for {
		if p := this.hpMin[0]; p.price == this.tMap[p.timestamp] {
			return p.price
		}
		heap.Pop(&this.hpMin)
	}
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */

type pair struct{ price, timestamp int }
type hp []pair

func (h hp) Len() int            { return len(h) }
func (h hp) Less(i, j int) bool  { return h[i].price <= h[j].price }
func (h hp) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v interface{}) { *h = append(*h, v.(pair)) }
func (h *hp) Pop() interface{}   { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func main() {

}
