package main

import "container/list"

type entry struct {
	key int
	val int
}

type LRUCache struct {
	capacity int
	n        int
	list     *list.List
	k2node   map[int]*list.Element
}

func Constructor(capacity int) LRUCache {
	return LRUCache{capacity, 0, list.New(), map[int]*list.Element{}}
}

func (this *LRUCache) Get(key int) int {
	node := this.k2node[key]
	if node == nil {
		return -1
	}
	this.list.MoveToBack(node)
	return node.Value.(entry).val
}

func (this *LRUCache) Put(key int, value int) {
	node := this.k2node[key]
	if node == nil {
		this.k2node[key] = this.list.PushBack(entry{key, value})
		if this.n < this.capacity {
			this.n++
		} else {
			frontNode := this.list.Front()
			delete(this.k2node, frontNode.Value.(entry).key)
			this.list.Remove(frontNode)
		}
	} else {
		node.Value = entry{key, value}
		this.list.MoveToBack(node)
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
