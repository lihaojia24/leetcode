package main

import (
	"fmt"
	"sync"
)

type School struct {
	name string
	id   int
}

var (
	instance *School
	once     sync.Once
	wg       sync.WaitGroup
)

func GetInstance(name string, id int) *School {
	once.Do(func() {
		instance = &School{}
		instance.name = name
		instance.id = id
	})
	return instance
}

func main() {
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			instance = GetInstance("hh", id)
			fmt.Printf("instance: %v\n", instance)
		}(i)
	}
	wg.Wait()
	println("end!")
}
