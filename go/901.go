package main

import "math"

type pair901 struct {
	day   int
	price int
}

type StockSpanner struct {
	stack  []pair901
	curDay int
}

func Constructor901() StockSpanner {
	return StockSpanner{[]pair901{{-1, math.MaxInt}}, -1}
}

func (this *StockSpanner) Next(price int) int {
	for price >= this.stack[len(this.stack)-1].price {
		this.stack = this.stack[:len(this.stack)-1]
	}
	this.curDay++
	this.stack = append(this.stack, pair901{this.curDay, price})
	return this.curDay - this.stack[len(this.stack)-2].day
}
