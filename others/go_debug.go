// go build go_debug.go
// GODEBUG=schedtrace=1000 ./go_debug
// GODEBUG=scheddetail=1,schedtrace=1000 ./go_debug

package main

import "time"

func main() {
	for i := 0; i < 3; i++ {
		time.Sleep(time.Second)
		println("ss")
	}
}
