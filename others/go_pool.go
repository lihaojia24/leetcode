package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type a struct {
	a int
	b string
	c float32
}

func main() {
	sp := sync.Pool{
		New: func() any {
			return a{a: rand.Int()}
		},
	}
	data := sp.Get().(a)
	data2 := sp.Get().(a)
	data3 := sp.Get().(a)
	data4 := sp.Get().(a)
	data5 := sp.Get().(a)
	fmt.Printf("data: %v\n", &data)
	fmt.Printf("data2: %v\n", &data2)
	fmt.Printf("data3: %v\n", &data3)
	fmt.Printf("data4: %v\n", &data4)
	fmt.Printf("data5: %v\n", &data5)
	sp.Put(data)
	sp.Put(data2)
	sp.Put(data3)
	// sp.Put(data4)
	// sp.Put(data5)
	time.Sleep(time.Second * 2)
	datax := sp.Get().(a)
	fmt.Printf("datax: %v\n", &datax)
}
