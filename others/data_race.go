package main

import (
	"fmt"
	"time"
)

// go run -race data_race.go
func main() {
	num := 0
	for i := 0; i < 1; i++ {
		go func() {
			num++
		}()
	}
	time.Sleep(time.Second)
	fmt.Printf("num: %v\n", num)
}
