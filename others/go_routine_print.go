package main

import "fmt"

func main() {
	const (
		GO_ROUTINE_NUM = 8
		MAX_PRINT_SIZR = 20
	)
	exit_chan := make(chan int)
	go_routines := []chan int{}
	for i := 0; i < GO_ROUTINE_NUM; i++ {
		go_routines = append(go_routines, make(chan int))
	}

	for i := 0; i < GO_ROUTINE_NUM; i++ {
		go func(i int) {
			for {
				num := <-go_routines[i]
				if num > MAX_PRINT_SIZR {
					exit_chan <- 1
					break
				}
				fmt.Printf("go_routine %v print num: %v\n", i, num)
				go_routines[(i+1)%GO_ROUTINE_NUM] <- num + 1
			}
		}(i)
	}

	go_routines[0] <- 1

	select {
	case <-exit_chan:
		fmt.Println("Done!")
	}
}
