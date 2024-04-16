package main

type MyHashMap []int

func Constructor12131() MyHashMap {
	return make([]int, 1_000_001)
}

func (this MyHashMap) Put(key int, value int) {
	this[key] = value + 1
}

func (this MyHashMap) Get(key int) int {
	return this[key] - 1
}

func (this MyHashMap) Remove(key int) {
	this[key] = 0
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */
