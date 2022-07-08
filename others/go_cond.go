package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	cond := sync.NewCond(&sync.Mutex{})
	flag := false
	for i := 0; i < 10; i++ {
		go func(i int) {
			cond.L.Lock()
			for !flag {
				cond.Wait()
			}
			cond.L.Unlock()
			fmt.Printf("i: %v\n", i)
		}(i)
	}
	time.Sleep(time.Second * 2)
	cond.L.Lock()
	flag = true
	cond.Broadcast()
	cond.L.Unlock()
	time.Sleep(time.Second * 2)
}
