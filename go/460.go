package main

import "container/list"

type lfuEntry struct {
	key, val int
	freq     int
}

type LFUCache struct {
	cap     int
	n       int
	minFreq int
	k2node  map[int]*list.Element
	f2list  map[int]*list.List
}

func ConstructorLFU(capacity int) LFUCache {
	return LFUCache{capacity, 0, 0, map[int]*list.Element{}, map[int]*list.List{}}
}

func (lfu *LFUCache) insert(entry *lfuEntry) {
	newList := lfu.f2list[entry.freq]
	if newList == nil {
		newList = list.New()
		lfu.f2list[entry.freq] = newList
	}
	node := newList.PushFront(entry)
	lfu.k2node[entry.key] = node
}

func (lfu *LFUCache) increaseFreq(node *list.Element) {
	entry := node.Value.(*lfuEntry)
	oldList := lfu.f2list[entry.freq]
	oldList.Remove(node)
	if entry.freq == lfu.minFreq && oldList.Len() == 0 {
		lfu.minFreq++
	}
	entry.freq++
	lfu.insert(entry)
}

func (lfu *LFUCache) remove() {
	l := lfu.f2list[lfu.minFreq]
	node := l.Back()
	l.Remove(node)
	delete(lfu.k2node, node.Value.(*lfuEntry).key)
}

func (lfu *LFUCache) Get(key int) int {
	node := lfu.k2node[key]
	if node == nil {
		return -1
	}
	lfu.increaseFreq(node)
	return node.Value.(*lfuEntry).val
}

func (lfu *LFUCache) Put(key int, value int) {
	node := lfu.k2node[key]
	if node != nil {
		node.Value.(*lfuEntry).val = value
		lfu.increaseFreq(node)
	} else {
		if lfu.cap == lfu.n {
			lfu.remove()
			lfu.n--
		}
		lfu.n++
		lfu.insert(&lfuEntry{key, value, 1})
		lfu.minFreq = 1
	}
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
